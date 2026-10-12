# AI for Dummies

Single-file static site: everything is in `index.html` (HTML, CSS, JS). Serve with `python3 -m http.server`.

## "Under the hood" demo (JS near the bottom of index.html)
- `PLANS` (regex → scripted reply, optional `think` / `tool`) defines each suggested prompt; `MSGS` lists the chips.
- `send()` runs the chat; `H.run()` plays the hood animation for the same turn (`H.turn` queues it if the hood is closed).
- `seen = {first, tool, think}`: what the viewer has already watched explained. First-time explanations play once; later turns skip them (`quick = seen.first`). `resetChat` clears every key automatically, so a new first-time explanation = add a key to `seen` + check it in `H.run`.
- `tell()`/`tips()`: bubbles are skipped in fast mode (set `window.tipsFast = true` to test them).

## Testing gotchas
- `send()` and `resetChat()` silently return while `busy` (the chat's own typing) is true; wait for it to clear between steps.
- Slow mode takes minutes; to test, scale `setTimeout` and `Element.prototype.animate` durations down, wrap `callout` to log bubble text, and poll results (long single Playwright calls get killed).
