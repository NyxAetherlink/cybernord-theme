# CyberNord

Nord Polar Night under a void-black base, with one electric cyan accent family.

This is the public specification and a first set of ports. It is early: tokens are stable enough to use, several ports are stubs, and more apps will land over time.

## Palette

| Role | Hex | Notes |
| :--- | :--- | :--- |
| Cyan glow | `#00e5ff` | Cursor, active, primary accent |
| Cyan mid | `#00b4d8` | Hover, secondary |
| Cyan deep | `#0077b6` | Selection, borders |
| Cyan light | `#48cae4` | Tags, inactive selection |
| Background | `#0d1117` | Window / void |
| Surface | `#2e3440` | Nord0 — sidebars, cards |
| Muted | `#4c566a` | Nord3 — comments, borders |
| Foreground | `#d8dee9` | Nord4 — body text |
| Bright FG | `#eceff4` | Nord6 — headings |
| Red / green / yellow / purple | Nord aurora | Errors, success, warn, magenta |

Canonical files: `tokens/cybernord.css`, `tokens/cybernord.json`.

## Ports

| Target | Path | Status |
| :--- | :--- | :--- |
| CSS variables | `tokens/cybernord.css` | Ready |
| JSON / SCSS / Tailwind v3 | `tokens/` | Ready |
| 16-color ANSI | `tokens/ansi-16.txt` | Ready |
| Obsidian (Shiba Inu overlay + Style Settings) | `ports/obsidian/` | Usable |
| Ghostty | `ports/ghostty/CyberNord` | Usable |
| Alacritty | `ports/alacritty/cybernord.toml` | Usable |
| VS Code | `ports/vscode/` | Stub (bg / fg / cursor only) |

### Obsidian

Requires [Shiba Inu](https://github.com/solderneer/shiba-inu-obsidian) and [Style Settings](https://github.com/mgmeyers/obsidian-style-settings).

1. Copy `ports/obsidian/cybernord-shiba-overlay.css` into the vault `snippets` folder and enable it.
2. Optionally import `ports/obsidian/obsidian-style-settings-cybernord.json` via Style Settings.

## License

MIT. See `LICENSE`.
