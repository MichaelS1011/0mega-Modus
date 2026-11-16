# README assets

Hand-authored SVG. One palette across all files: `#8C1E14` brand red, `#EADCC4` cream,
`#F7F0E2` tint, `#4A120C` ink, `#24100B` dark paper, `#C87B66` cream-red (dark mode).
Typography is the system Helvetica/Arial stack, so nothing has to be bundled.

| File | viewBox | Used for |
|---|---|---|
| `logo-mark.svg` / `logo-mark-dark.svg` | 128×128 | Slashed-O mark on cream / dark paper |
| `logo-horizontal.svg` / `logo-horizontal-dark.svg` | 480×120 | Mark plus wordmark, light / dark |
| `diagram-how-it-works.svg` | 1200×520 | Request → assess → mode → seven functions → approval gate |
| `diagram-rigor-dial.svg` | 1000×480 | The three modes as a proportionality scale |
| `diagram-adapters.svg` | 1000×360 | The seven adapters and where their instructions live |

Diagrams carry their own opaque background, so they read correctly on GitHub light and dark
(README embeds them as `<img>`, where `prefers-color-scheme` inside an SVG would not apply).
The logos come in a light and a dark variant, selected with `<picture>`.

Edit the SVGs directly; they are plain text. Verify a change by opening the file in a browser
before committing.
