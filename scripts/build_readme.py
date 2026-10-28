#!/usr/bin/env python3
"""Rebuild the scoreboard section of README.md from data/tracker.csv.

Usage:
    python3 scripts/build_readme.py              # as of today (Europe/London)
    python3 scripts/build_readme.py 2026-10-28   # as of a given date
    python3 scripts/build_readme.py --check      # exit 1 if README is out of date

Everything between the two marker comments in README.md is replaced:
    <!-- SCOREBOARD:START -->  ...  <!-- SCOREBOARD:END -->
Nothing outside the markers is touched.

Rules applied here (the verdicts themselves live in the CSV):
  * rows without a source link (post_url starting with http) are skipped
  * overdue days are recomputed from deadline_date to the as-of date
  * late days come from the CSV's days_late column
  * vague rows are listed but never scored
  * on-time % = on time / (on time + late + overdue)
"""
import csv, os, sys
from datetime import date, datetime
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "data", "tracker.csv")
README = os.path.join(ROOT, "README.md")
START, END = "<!-- SCOREBOARD:START -->", "<!-- SCOREBOARD:END -->"
MAXQ = 90


def d(s):
    return date.fromisoformat(s) if s else None


def fmt(dt_):
    return f"{dt_.day} {dt_.strftime('%b %Y')}" if dt_ else "–"


def cell(s):
    return s.replace("|", "\\|").replace("\n", " ").strip()


def short(q):
    q = q.strip()
    if len(q) > MAXQ:
        q = q[:MAXQ].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
    return cell(q)


def link(url, label):
    return f"[{label}]({url})" if url.startswith("http") else "–"


def promise_link(url):
    return link(url, "post" if "x.com/" in url or "twitter.com/" in url else "source")


def plural(n, word):
    return f"{n} {word}{'' if n == 1 else 's'}"


def load(today):
    rows = []
    with open(CSV_PATH, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r["post_url"].strip().startswith("http"):
                continue
            r["_deadline"] = d(r["deadline_date"])
            r["_shipped"] = d(r["shipped_date"])
            r["_days"] = None
            if r["status"] == "overdue" and r["_deadline"]:
                r["_days"] = (today - r["_deadline"]).days
            elif r["status"] == "shipped_late" and r["days_late"]:
                r["_days"] = int(r["days_late"])
            rows.append(r)
    return rows


def table(rows, status_fn):
    out = ["| company | promise | promised | deadline | verdict | sources |",
           "|---|---|---|---|---|---|"]
    for r in rows:
        src = promise_link(r["post_url"])
        if r["shipped_source_url"].startswith("http"):
            src += " · " + link(r["shipped_source_url"], "shipped")
        out.append(f"| {cell(r['company'])} | {short(r['quote'])} | {cell(r['promised_timeframe'])} "
                   f"| {fmt(r['_deadline'])} | {status_fn(r)} | {src} |")
    return out


def build(today):
    rows = load(today)
    by = {s: [r for r in rows if r["status"] == s]
          for s in ("overdue", "shipped_late", "pending", "shipped_on_time", "vague")}
    on, late, over = len(by["shipped_on_time"]), len(by["shipped_late"]), len(by["overdue"])
    scored = on + late + over
    pct = round(100 * on / scored) if scored else 0

    L = [START, "",
         f"_last updated {fmt(today)} (UK). generated from [`data/tracker.csv`](data/tracker.csv) "
         f"by [`scripts/build_readme.py`](scripts/build_readme.py)._", "",
         f"**{len(rows)} promises tracked: {on} on time, {late} late, {over} overdue, "
         f"{len(by['pending'])} pending, {len(by['vague'])} vague (not scored).**", "",
         f"**on-time rate: {pct}%** ({on} of {scored} promises whose deadline has passed or that already shipped).", ""]

    L += ["### overdue", "", "deadline's gone, no sign of it.", ""]
    L += table(sorted(by["overdue"], key=lambda r: -(r["_days"] or 0)),
               lambda r: f"🔴 {plural(r['_days'], 'day')} overdue")
    L += ["", "### late", "", "got there in the end.", ""]
    L += table(sorted(by["shipped_late"], key=lambda r: -(r["_days"] or 0)),
               lambda r: f"🟠 {plural(r['_days'], 'day')} late (shipped {fmt(r['_shipped'])})")
    L += ["", "### pending", "", "clock's ticking.", ""]

    def pend(r):
        left = (r["_deadline"] - today).days
        if left > 0:
            return f"⏳ {plural(left, 'day')} left"
        return "⏳ due today" if left == 0 else "⏳ deadline passed, awaiting check"
    L += table(sorted(by["pending"], key=lambda r: r["_deadline"]), pend)
    L += ["", "### on time", "", "credit where it's due.", ""]
    L += table(sorted(by["shipped_on_time"], key=lambda r: r["_shipped"] or date.min, reverse=True),
               lambda r: f"✅ shipped {fmt(r['_shipped'])}")
    L += ["", "### vague (not scored)", "",
          "no date, no deadline, no score. listed so you can see what we left out, and whether it turned up anyway.", "",
          "| company | promise | wording | what happened | sources |", "|---|---|---|---|---|"]
    for r in sorted(by["vague"], key=lambda r: r["post_date"]):
        src = promise_link(r["post_url"])
        if r["shipped_source_url"].startswith("http"):
            src += " · " + link(r["shipped_source_url"], "shipped")
        what = f"shipped {fmt(r['_shipped'])}" if r["_shipped"] else "not out yet"
        L.append(f"| {cell(r['company'])} | {short(r['quote'])} | {cell(r['promised_timeframe'])} | {what} | {src} |")
    L += ["", END]
    return "\n".join(L)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    today = d(args[0]) if args else datetime.now(ZoneInfo("Europe/London")).date()
    text = open(README, encoding="utf-8").read()
    i, j = text.find(START), text.find(END)
    if i < 0 or j < i:
        sys.exit("README.md is missing the SCOREBOARD markers")
    new = text[:i] + build(today) + text[j + len(END):]
    if "--check" in sys.argv:
        sys.exit(0 if new == text else 1)
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
        print(f"README.md scoreboard updated (as of {today})")
    else:
        print("README.md already up to date")


if __name__ == "__main__":
    main()
