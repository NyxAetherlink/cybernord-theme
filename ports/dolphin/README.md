# CyberNord for Dolphin

KDE color scheme for Dolphin (and other Breeze/Qt apps that read
`kdeglobals`). Dolphin has no stylesheet; this is the native lever.

## What it maps

| Role | Token | KDE group |
| :--- | :--- | :--- |
| File view canvas | void `#0d1117` | Colors:View / Window |
| Alternate rows / inactive header | lifted `#161b22` | View BackgroundAlternate |
| Toolbars, places, buttons | surface `#2e3440` | Header, Complementary, Button |
| Selected row | cyan deep `#0077b6` | Colors:Selection |
| Focus / hover | glow `#00e5ff` / mid `#00b4d8` | DecorationFocus / Hover |
| Status | aurora | Negative / Positive / Neutral |

Standout: **selection + focus ring** are the one lit control. KDE cannot
draw a 2px CSS rail; if the window still looks like grey Nord, selection
never applied (see install).

## Install

```bash
mkdir -p ~/.local/share/color-schemes
cp CyberNord.colors ~/.local/share/color-schemes/
kwriteconfig6 --file dolphinrc --group UiSettings --key ColorScheme CyberNord
```

On Sway / without Plasma, Qt still paints from `~/.config/kdeglobals`.
Merge the scheme into that file (keeps non-color groups):

```bash
python3 merge-into-kdeglobals.py
```

Restart Dolphin after.

## Host limits

- No per-panel cyan hairline. Icon glyphs (folder blue) come from the
  **icon theme**, not this scheme.
- Titlebar colors in `[WM]` only apply under KWin; Sway ignores them.
- Changing `kdeglobals` also tints Kate, Okular, and other KDE apps.
