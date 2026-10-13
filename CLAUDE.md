# AI for Dummies

Single-file static site: everything is in `index.html` (HTML, CSS, JS). Serve with `python3 -m http.server`.

## "Under the hood" demo (JS near the bottom of index.html)
- `PLANS` (regex → scripted reply, optional `think` / `tool`) defines each suggested prompt; `MSGS` lists the chips.
- `send()` runs the chat; `H.run()` plays the hood animation for the same turn (`H.turn` queues it if the hood is closed).
- `seen = {first, tool, think}`: what the viewer has already watched explained. First-time explanations play once; later turns skip them (`quick = seen.first`). `resetChat` clears every key automatically, so a new first-time explanation = add a key to `seen` + check it in `H.run`.
- The hood's orange "i" buttons (`.hi`, plus the notebook's `#hpin`) open the same `openTip` modal as the chat's `.ipin` pins; `data-k` is a key in `spots` (add one in `spots` for a new part). Opening one calls `hoodHold()` (pauses the demo, hides its bubble) and `closeTip` calls `hoodRelease()`. Demo bubbles (`tell()` → `callout(id, text, true)`) get a Next button with a countdown (`go(ms, true)`; `H.skip`). Nothing else in the hood is clickable.
- `tell()`/`tips()`: bubbles are skipped in fast mode (set `window.tipsFast = true` to test them).

## Page chrome
- Sticky tab bar `#viewbar`: the router only handles `a[data-view]` tabs. The "buy me a coffee" link (`a.coffee`, also in the footer) is a plain external link: its own centred line under the tabs at 721px+, a short pill on the tab row at 720px and below (where the tabs already wrap, so the bar never gains a row).

## Testing gotchas
- `send()` and `resetChat()` silently return while `busy` (the chat's own typing) is true; wait for it to clear between steps.
- Slow mode takes minutes; to test, scale `setTimeout` and `Element.prototype.animate` durations down, wrap `callout` to log bubble text, and poll results (long single Playwright calls get killed).
