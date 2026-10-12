# Idea: optional visualizations for the headline debunks

Status: idea only, nothing started.

## Why

Several headlines turn on one point: the model can only ask, and the harness (plain, deterministic code with permissions) decides. Claude Code is the real-world example: settings strictly limit files and tools, the model can ask all it likes and be refused, and it often treats a refusal as an obstacle and asks for a different tool instead of giving up. Text explains this; a small interactive picture would make it obvious.

## What

An optional "Show me" button inside a headline's "Break it down" panel. Closed by default so the page stays light and the text still works alone. It opens a small version of the under-the-hood diagram (You / Harness / Model / Tools) wired to that story, with one control the viewer can flip, such as a permission switch on the harness (allow / ask first / deny).

## Best-fit headlines

- "AI refuses to be turned off": the off switch lives in the harness, outside the model. Show a stop request the model can't override.
- "AI deleted a company's database": give the tool too much power vs. permissions, approval prompts and backups. Flip the switch and watch the same request get blocked or confirmed.
- "AI broke out of its sandbox": leaky vs. sealed containment. Same request, different outcome.
- "AI blackmails engineers": shows which access was handed over (email send). Remove the permission and the scheme has nothing to act with.
- Maybe: "AI lies, schemes, copies itself" (copying needs write access somebody granted).

## Core scenario to build once

Model asks for a tool → harness checks permissions → allowed or denied → on denial the model tries a different tool. This is the same flow as the weather demo plus a denial and a retry, so most of the pieces already exist.

## Plan

1. Refactor: pull the hood's diagram, `fly` and `callout` helpers into something a second, smaller instance can reuse (today they assume the single `#engine` panel). This is the main cost and risk.
2. Add a data-driven scenario format (steps: who talks to whom, label, whether the harness allows it, optional retry). Keep scenarios as plain data so a new headline is a new entry, not new animation code.
3. Build the shared "Show me" widget with the permission switch and a replay button.
4. Add it to one headline first (database deletion is probably the clearest) and check it works on phone widths.
5. Roll out to the others only where it genuinely helps; skip any where a picture adds nothing.

## Open questions

- Reuse the exact hood visuals or a simplified cut-down version?
- Does it respect the Slow/Fast switch, and the reduced-motion setting (needs a static fallback)?
- Where does the widget live in the page markup so it stays lazy (nothing runs until opened)?
