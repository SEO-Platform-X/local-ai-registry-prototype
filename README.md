# Local AI Registry: design prototype

Clickable design prototype for localairegistry.com, desktop and mobile.

## What is here

- `prototype/` : every screen as a single HTML file (`*.dc.html`), plus `canvas.json`, which lays the boards out as journeys.
  Open `prototype/Flow.dc.html` first. It maps every screen to its journey and links to the mobile boards.
- `generators/` : the Python scripts that produced the boards. They are a record of how each screen was built, not production code.
  They use absolute paths from the build environment and will need their paths updated before they run anywhere else.
- `generators/mobile/` : the scripts for the mobile boards (M1 to M8).

## Notes for the developer

- Boards ending in `_p2`, `_p3` and so on are slices of one tall page, made so the prototype opens on phones.
  The full page lives in the file without the suffix (for example, `Home.dc.html` is the whole homepage).
- Boards titled "Unused · safe to delete" are retired and can be removed.
- Start with `Flow.dc.html`, `FlowBuild.dc.html` (rebuild prompt and design system) and `FlowRules.dc.html` (product rules and open items).
