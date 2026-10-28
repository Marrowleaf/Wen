<p align="center">
  <img src="assets/banner.png" alt="wen: &quot;coming soon.&quot; cool. but wen?" width="100%">
</p>

<p align="center">
  <a href="https://x.com/wenreport"><img src="https://img.shields.io/badge/follow-%40wenreport-F75347?style=for-the-badge&logo=x&logoColor=white" alt="follow @wenreport on X"></a>
  <a href="https://x.com/marrowleaf"><img src="https://img.shields.io/badge/built%20by-%40marrowleaf-111111?style=for-the-badge&logo=x&logoColor=white" alt="built by @marrowleaf on X"></a>
</p>

# wen?

**"coming soon." cool. but wen?**

wen keeps score on the timed promises companies make on X. "in the coming weeks", "later this year", "this summer", "next month". we write down what was promised and when, work out the deadline, and check whether it actually turned up on time.

on time, late, overdue. with receipts.

live verdicts, new promises and the weekly monday wen report go out on X at **[@wenreport](https://x.com/wenreport)**.

## how it works

1. **spot a promise.** a company (or someone clearly speaking for it) says something's coming within a stated window.
2. **log it.** company, the exact wording, a link to the source, and the date it was said.
3. **set the deadline.** turn the wording into a calendar date using the house rules below. same rules for everyone.
4. **check back.** when it ships we log the date and a link proving it. if the deadline passes with no sign of it, it's overdue and the days start counting.

everything lives in [`data/tracker.csv`](data/tracker.csv), one row per promise, with notes on what was checked and any caveats. the scoreboard below is generated from that file.

## house rules

**only timed promises count.** "coming soon" with no window isn't a promise, it's a vibe. those go in the vague list and never get scored.

**no link, no row.** every promise needs a clear source link to what was actually said. every "shipped" needs a link showing it shipped.

**we never invent dates or claims.** if we can't find it, we say so. if it's unclear, the notes say it's unclear.

**deadlines are read generously, on purpose:**

| they said | deadline |
|---|---|
| "in the coming weeks" / "next few weeks" | post date + 8 weeks |
| "next week" | the sunday at the end of the following mon–sun week |
| "next month" | last day of the following month |
| a named month ("this august", "shipping in november") | last day of that month |
| "early YYYY" | 30 apr |
| "mid YYYY" | 31 aug |
| "late YYYY" / "this year" / "later this year" | 31 dec |
| seasons (spring / summer / fall / winter) | end of the astronomical season: 20 jun / 22 sep / 20 dec / 20 mar |
| "Q1"–"Q4 YYYY" | last day of the quarter |
| "tomorrow" / "today" | end of that day in the poster's own time zone |
| "in the next 24hr" | post time + 24 hours |
| an exact date | that date |
| "soon" / "coming soon" / no window | vague, not scored |

**how verdicts are decided:**

- ✅ **on time**: shipped on or before the deadline, with a source.
- 🟠 **late**: shipped after the deadline, with a source. days late = ship date minus deadline.
- 🔴 **overdue**: deadline passed and we can't find any evidence it shipped. days overdue keep counting until it does.
- ⏳ **pending**: deadline not reached yet.
- **vague**: no scoreable window. listed, never scored.

we score what was actually promised. if they said "generally available", a preview doesn't count (but we'll mention it). partial or regional launches go in the notes. on-time rate = on time ÷ (on time + late + overdue); pending and vague don't count either way.

## the scoreboard

<!-- SCOREBOARD:START -->

_last updated 28 Oct 2026 (UK). generated from [`data/tracker.csv`](data/tracker.csv) by [`scripts/build_readme.py`](scripts/build_readme.py)._

**44 promises tracked: 21 on time, 3 late, 4 overdue, 11 pending, 5 vague (not scored).**

**on-time rate: 75%** (21 of 28 promises whose deadline has passed or that already shipped).

### overdue

deadline's gone, no sign of it.

| company | promise | promised | deadline | verdict | sources |
|---|---|---|---|---|---|
| Rockstar Games | Grand Theft Auto VI is now set to release on May 26, 2026. | May 26, 2026 | 26 May 2026 | 🔴 155 days overdue | [post](https://x.com/RockstarGames/status/1918265468076605706) |
| PlayStation | The FlexStrike wireless fight stick and PlayStation 27’’ Gaming Monitor launch this August | this August | 31 Aug 2026 | 🔴 58 days overdue | [post](https://x.com/PlayStation/status/2061462930864910415) |
| Uber | Starting this summer in Las Vegas and next year in Los Angeles, Uber riders can get… | this summer (Las Vegas) | 22 Sep 2026 | 🔴 36 days overdue | [post](https://x.com/Uber/status/2031717139715928492) |
| Nintendo | Kyoto Xanadu, a brand-new action RPG from @nihonfalcom, is coming this summer on Nintendo… | this summer | 22 Sep 2026 | 🔴 36 days overdue | [post](https://x.com/NintendoAmerica/status/2019415907945128016) |

### late

got there in the end.

| company | promise | promised | deadline | verdict | sources |
|---|---|---|---|---|---|
| Google | Ironwood, our most powerful and energy-efficient Tensor Processing Unit (TPU) yet, will… | in the coming weeks | 1 Jan 2026 | 🟠 89 days late (shipped 31 Mar 2026) | [post](https://x.com/Google/status/1986537172770390389) · [shipped](https://docs.cloud.google.cn/tpu/docs/release-notes) |
| Xbox | Then get ready for DAVE THE DIVER: In the Jungle DLC in early 2026 | early 2026 | 30 Apr 2026 | 🟠 49 days late (shipped 18 Jun 2026) | [post](https://x.com/XBOX/status/1991568935469355417) · [shipped](https://www.gematsu.com/2026/03/dave-the-diver-dlc-in-the-jungle-launches-june-18) |
| Xbox | Gaming Copilot (Beta) is starting to roll out on PC Game Bar today and the Xbox mobile… | next month (Oct 2025) | 31 Oct 2025 | 🟠 25 days late (shipped 25 Nov 2025) | [post](https://x.com/XBOX/status/1968706674643882324) · [shipped](https://news.xbox.com/en-us/2025/11/25/xbox-november-update-gaming-copilot-full-screen-experience/) |

### pending

clock's ticking.

| company | promise | promised | deadline | verdict | sources |
|---|---|---|---|---|---|
| Apple | Customers can pre-order the new 14-inch MacBook Pro with M6 starting tomorrow, October… | starting tomorrow, October 28 | 29 Oct 2026 | ⏳ 1 day left | [source](https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/) |
| Moonshot AI | Full model weights will be released by Nov 4, 2026. | by Nov 4, 2026 | 4 Nov 2026 | ⏳ 7 days left | [source](https://www.kimi.ai/blog/kimi-k3-1-pro) |
| Apple | It will begin arriving to customers, and in Apple Store locations and Apple Authorized… | starting Friday, November 6 | 7 Nov 2026 | ⏳ 10 days left | [source](https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/) |
| VX Framework | This is the last release before 1.0, which will be next week. | next week | 8 Nov 2026 | ⏳ 11 days left | [post](https://x.com/VX_Framework/status/2115043522042540505) |
| Rockstar Games | Grand Theft Auto VI will now release on Thursday, November 19, 2026. | Thursday, November 19, 2026 | 19 Nov 2026 | ⏳ 22 days left | [post](https://x.com/RockstarGames/status/1986540361011880167) |
| Tesla | In fact, next month, we'll be launching in Dallas and then the same software just scaled… | next month (Dallas Cybercab) | 30 Nov 2026 | ⏳ 33 days left | [source](https://www.fool.com/earnings/call-transcripts/2026/10/22/tesla-tsla-q3-2026-earnings-call-transcript/) |
| PlayStation | PlayStation: The First 30 Years is available to order now, shipping in November | shipping in November | 30 Nov 2026 | ⏳ 33 days left | [post](https://x.com/PlayStation/status/2115103862235488669) |
| Google | Coming first this fall: audio glasses designed to give you help from Gemini to take… | this fall | 20 Dec 2026 | ⏳ 53 days left | [post](https://x.com/Google/status/2056805831237386360) |
| Nintendo | The Legend of Zelda: Ocarina of Time is coming to #NintendoSwitch2 later this year. | later this year | 31 Dec 2026 | ⏳ 64 days left | [post](https://x.com/NintendoUK/status/2064360851235033255) |
| Tesla | we're trying to get Cybercabs to customers by the end of this year, 2026. | end of this year, 2026 | 31 Dec 2026 | ⏳ 64 days left | [source](https://www.fool.com/earnings/call-transcripts/2026/10/22/tesla-tsla-q3-2026-earnings-call-transcript/) |
| PlayStation | Conan Exiles Enhanced and Aloft launch on PS5 in early 2027 | early 2027 | 30 Apr 2027 | ⏳ 184 days left | [post](https://x.com/PlayStation/status/2115111881153368322) |

### on time

credit where it's due.

| company | promise | promised | deadline | verdict | sources |
|---|---|---|---|---|---|
| Artificial Analysis | Tomorrow. | tomorrow | 28 Oct 2026 | ✅ shipped 28 Oct 2026 | [post](https://x.com/ArtificialAnlys/status/2114889320012333423) · [shipped](https://x.com/ArtificialAnlys/status/2115265133467635877) |
| Google | Be on the lookout for the update in the next 24hr! | in the next 24hr | 28 Oct 2026 | ✅ shipped 26 Oct 2026 | [post](https://x.com/rodydavis/status/2114878923360342066) · [shipped](https://antigravity.google/docs/changelog/#rel-ide-2.6.0) |
| Google | Introducing Googlebook, the first laptop designed for Gemini Intelligence. It’s crafted… | this fall | 20 Dec 2026 | ✅ shipped 4 Oct 2026 | [post](https://x.com/Google/status/2054270454467121187) · [shipped](https://www.androidauthority.com/googlebook-availability-release-freebies-3713298/) |
| PlayStation | State of Play just debuted a extended look at Control Resonant, coming to PS5 later this… | later this year | 31 Dec 2026 | ✅ shipped 24 Sep 2026 | [post](https://x.com/PlayStation/status/2022074133027385673) · [shipped](https://www.remedygames.com/article/control-resonant-launches-worldwide-on-september-24) |
| Tesla | Tesla Semi remains on track for volume production this year at our new factory in Nevada | this year | 31 Dec 2026 | ✅ shipped 24 Sep 2026 | [post](https://x.com/Tesla/status/2080021924072366329) · [shipped](https://electrek.co/2026/09/25/tesla-semi-volume-production-launch-nevada-factory/) |
| Uber | as we fine tune the experience ahead of the public launch in the coming weeks. | in the coming weeks | 15 Oct 2026 | ✅ shipped 3 Sep 2026 | [post](https://x.com/Uber/status/2090363210520256628) · [shipped](https://wayve.ai/press/wayve-uber-launch-autonomous-rides/) |
| Nintendo | @OrbitalsGame is coming exclusively to Nintendo Switch 2 this summer! | this summer | 22 Sep 2026 | ✅ shipped 3 Sep 2026 | [post](https://x.com/NintendoAmerica/status/2019411649627611148) · [shipped](https://www.orbitalsgame.com/post/orbitals-is-out-now-on-nintendo-switch-2) |
| Anthropic | Available on Max and Team today, rolling out to Pro in the coming weeks. | in the coming weeks | 7 Oct 2026 | ✅ shipped 26 Aug 2026 | [post](https://x.com/claudeai/status/2087635262390026525) · [shipped](https://x.com/claudeai/status/2092755574563741871) |
| Xbox | S.T.A.L.K.E.R. 2: Cost of Hope, the first major expansion, is coming Summer 2026 | Summer 2026 | 22 Sep 2026 | ✅ shipped 20 Aug 2026 | [post](https://x.com/XBOX/status/2037219046060679318) · [shipped](https://www.stalker2.com/news/cost-of-hope-release) |
| WhatsApp | starting this week, you can reserve a username to use later this year when we launch the… | later this year | 31 Dec 2026 | ✅ shipped 7 Jul 2026 | [post](https://x.com/WhatsApp/status/2071627237095354410) · [shipped](https://www.useinvent.com/blog/whatsapp-usernames-explained-what-businesses-need-to-know) |
| Google | In the coming weeks, we’ll be bringing Gemini Spark to the Gemini desktop app | in the coming weeks | 14 Jul 2026 | ✅ shipped 30 Jun 2026 | [post](https://x.com/GeminiApp/status/2056802363269329304) · [shipped](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/) |
| Starlink | Starting this summer, Starlink will deliver high-speed internet onboard @SouthwestAirlines | this summer | 22 Sep 2026 | ✅ shipped 22 Jun 2026 | [post](https://x.com/Starlink/status/2021707118072500660) · [shipped](https://airlinegeeks.com/2026/06/23/southwests-first-starlink-equipped-aircraft-enters-service/) |
| Xbox | get fired up for the throwdown when Kiln comes Spring 2026 | Spring 2026 | 20 Jun 2026 | ✅ shipped 23 Apr 2026 | [post](https://x.com/XBOXGamePass/status/2014407146432352638) · [shipped](https://store.steampowered.com/app/1165990/Kiln/) |
| PlayStation | Johnny Rico welcomes you to Starship Troopers: Ultimate Bug War, a retro FPS arriving… | early 2026 | 30 Apr 2026 | ✅ shipped 16 Mar 2026 | [post](https://x.com/PlayStation/status/1996682006466318408) · [shipped](https://blog.playstation.com/2026/03/03/play-as-the-bugs-in-starship-troopers-ultimate-bug-war-out-march-16/) |
| Xbox | Fatal Frame II: Crimson Butterfly Remake is coming early 2026 | early 2026 | 30 Apr 2026 | ✅ shipped 12 Mar 2026 | [post](https://x.com/XBOX/status/1971243307670900880) · [shipped](https://www.koeitecmoamerica.com/news/the-screams-of-classic-japanese-horror-await-as-fatal-frame-ii-crimson-butterfly-remake-returns-march-12-2026/) |
| OpenAI | In the coming weeks, we plan to start testing ads in ChatGPT free and Go tiers. | in the coming weeks | 13 Mar 2026 | ✅ shipped 9 Feb 2026 | [post](https://x.com/OpenAI/status/2012223373489614951) · [shipped](https://openai.com/index/testing-ads-in-chatgpt/) |
| OpenAI | Later this year, we’ll begin accepting app submissions for publication. | later this year | 31 Dec 2025 | ✅ shipped 17 Dec 2025 | [post](https://x.com/OpenAIDevs/status/1975261988751351868) · [shipped](https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/) |
| PlayStation | New gameplay trailer for Thief VR: Legacy of Shadow shows how the stealth classic is… | later this year | 31 Dec 2025 | ✅ shipped 4 Dec 2025 | [post](https://x.com/PlayStation/status/1973074235313606961) · [shipped](https://www.vertigo-games.com/the-thief-franchise-returns-with-thief-vr-legacy-of-shadow-out-now/) |
| PlayStation | Available for purchase later this year, along with the free Spec III update | later this year | 31 Dec 2025 | ✅ shipped 4 Dec 2025 | [post](https://x.com/PlayStation/status/1988383864168088026) · [shipped](https://blog.playstation.com/2025/12/03/gran-turismo-7-spec-iii-power-pack-dlc-available-december-4/) |
| PlayStation | Pacific Drive expansion Whispers in the Woods rolls out later this year | later this year | 31 Dec 2025 | ✅ shipped 23 Oct 2025 | [post](https://x.com/PlayStation/status/1965475458524311556) · [shipped](https://news.xbox.com/en-us/2025/10/23/pacific-drive-xbox-launch-game-pass/) |
| Google | We’re rolling out a bunch of new features to #PixelBuds Pro 2 next month | next month (Sep 2025) | 30 Sep 2025 | ✅ shipped 25 Sep 2025 | [post](https://x.com/madebygoogle/status/1958221089118585283) · [shipped](https://9to5google.com/2025/09/25/pixel-buds-2-pro-update-sept-25/) |

### vague (not scored)

no date, no deadline, no score. listed so you can see what we left out, and whether it turned up anyway.

| company | promise | wording | what happened | sources |
|---|---|---|---|---|
| Perplexity | Coming soon to Android. | coming soon | shipped 17 Mar 2026 | [post](https://x.com/perplexity_ai/status/2032494752642568417) · [shipped](https://www.indiatoday.in/technology/news/story/perplexity-computer-on-android-what-is-it-how-to-use-and-everything-else-to-know-2883243-2026-03-17) |
| OpenAI | API is coming soon. | coming soon | shipped 24 Apr 2026 | [post](https://x.com/OpenAIDevs/status/2047377079352877534) · [shipped](https://developers.openai.com/api/docs/changelog) |
| OpenAI | GPT-6.1 Terra is also coming to the API and Codex. | coming to the API | shipped 26 Oct 2026 | [post](https://x.com/OpenAIDevs/status/2114780986613682473) · [shipped](https://developers.openai.com/api/docs/changelog) |
| Google DeepMind | before bringing the model to Google AI Ultra subscribers in Project Genie and early… | soon | not out yet | [post](https://x.com/GoogleDeepMind/status/2115114030503166385) |
| Google | coming soon to the API for the first time | coming soon | not out yet | [post](https://x.com/OfficialLoganK/status/2115129174826647863) |

<!-- SCOREBOARD:END -->

## tips and corrections

spotted a dated "coming soon"? tag **[@wenreport](https://x.com/wenreport)** with a link to the post. no link, no row.

think we got one wrong? same deal: tag us with a source and we'll fix it in public.

## refreshing the scoreboard

```
python3 scripts/build_readme.py            # as of today, UK time
python3 scripts/build_readme.py 2026-10-28 # as of a given date
python3 scripts/build_readme.py --check    # exits 1 if the README is stale
```

the script only rewrites the bit between the `SCOREBOARD` markers. python 3.9+, no dependencies.

---

<p align="center"><img src="assets/logo.png" alt="wen logo" width="96"><br>built in public by <a href="https://x.com/marrowleaf">@marrowleaf</a> · scores posted by <a href="https://x.com/wenreport">@wenreport</a></p>
