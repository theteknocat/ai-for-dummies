# AI for Dummies

Single-file static site: everything is in `index.html` (HTML, CSS, JS). Serve with `python3 -m http.server`.

## "Under the hood" demo (JS near the bottom of index.html)
- `PLANS` (regex → scripted reply, optional `think` / `tool`) defines each suggested prompt; `MSGS` lists the prompts, shown in the hood's custom dropdown (`#hpickbtn` + `#hchips` menu, not a `<select>`).
- `send()` runs the chat; `H.run()` plays the hood animation for the same turn (`H.turn` queues it if the hood is closed).
- `seen = {first, tool, think}`: what the viewer has already watched explained. First-time explanations play once; later turns skip them (`quick = seen.first`). `resetChat` clears every key automatically, so a new first-time explanation = add a key to `seen` + check it in `H.run`.
- `LIMIT` (tokens, deliberately tiny) caps the context; `FILL` (80%) is the refuse threshold, since a harness can't know a reply's length. `send()` refuses (sets `full`, fixed "limit reached" chat message, hood plays `H.run(text, {reject: true})`: red pulsing harness, bounced message, tooltip) once `used()` + the message passes `FILL`, and refuses everything until `resetChat`. A turn that still hits `LIMIT` is clipped (`p.cut`): the chat ends with a cut-off notice and the hood pulses red. Both put one token-free floating `.pg.notice` in the notebook (`H.notice`, kept across `resetPages`). Both chat notices carry an `.ipin` (`spots.limit`). The hood's notebook count shows `N of LIMIT`.
- While a turn runs (`H.cur` or `busy`), `chips()` locks the picker (it shows the running prompt, lit and animated), the speed switch and both Clear buttons: changing speed mid-turn is unsupported.
- Both message pickers (front `#cpickbtn`/`#cmenu`, hood `#hpickbtn`/`#hchips`) are custom button + popup lists made by `wireMenu()`, not `<select>`s. The front one reads `cval`/`setPick()` and opens upward when there's more room above. `match()` keeps the front of the hood (`#chatface`) as tall as the open engine so the lid fits exactly.
- Opening the hood (`hood(true)`) calls `fitHood()`: centres it under the sticky bar, or tops it there when it is taller than the room (phones). `body{overflow-x:clip}` (not `hidden`: that would break the sticky bar) stops the lifted lid enlarging phone layout viewports. The Pop button (`#flipbtn`) tucks away via a `.away` transform class, never `hidden`, so the page height stays fixed.
- Bubbles (`callout`) go below their box if they fit on screen, else above; demo bubbles focus their Next button so Enter skips.
- The hood's orange "i" buttons (`.hi`, plus the notebook's `#hpin`) open the same `openTip` modal as the chat's `.ipin` pins; `data-k` is a key in `spots` (add one in `spots` for a new part). Opening one calls `hoodHold()` (pauses the demo, hides its bubble) and `closeTip` calls `hoodRelease()`. Demo bubbles (`tell()` → `callout(id, text, true)`) get a Next button with a countdown (`go(ms, true)`; `H.skip`). Nothing else in the hood is clickable.
- `tell()`/`tips()`: bubbles are skipped in fast mode (set `window.tipsFast = true` to test them).

## Page chrome
- Sticky tab bar `#viewbar`: the router only handles `a[data-view]` tabs. The "buy me a coffee" link (`a.coffee`, also in the footer) is a plain external link: its own centred line under the tabs at 721px+, a short pill on the tab row at 720px and below (where the tabs already wrap, so the bar never gains a row).

## Testing gotchas
- `send()` and `resetChat()` silently return while `busy` (the chat's own typing) is true; wait for it to clear between steps.
- Slow mode takes minutes; to test, scale `setTimeout` and `Element.prototype.animate` durations down, wrap `callout` to log bubble text, and poll results (long single Playwright calls get killed).

## Analytics (Umami, stats.peter-epp.dev)
- Tracker `<script>` is at the end of `<head>`; `data-domains="ai-for-dummies.info"` keeps local runs untracked, `data-exclude-hash` stops anchor jumps counting as pageviews. The tracker auto-reports `pushState`/`replaceState` (tab clicks) but not `popstate` (Back/Forward) or outbound links, so the page does both itself.
- `track(name, data)` (near the router) wraps `umami.track` and is a no-op when blocked. Events: `message-sent` {where, text}, `hood-open`, `toc-click` {page, to}, `outbound-click` {url}.
