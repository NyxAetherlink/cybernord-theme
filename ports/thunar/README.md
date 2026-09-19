# CyberNord for Thunar

GTK3 overlay. Thunar does not use KDE color schemes.

## Install

```bash
cp colors.css thunar.css gtk.css ~/.config/gtk-3.0/
# optional: same colors.css for GTK4 apps
cp colors.css ~/.config/gtk-4.0/colors.css
```

Ensure `~/.config/gtk-3.0/settings.ini` has:

```
gtk-application-prefer-dark-theme=true
```

Restart Thunar (`thunar -q`).

## Visual system

- **Lifted-void file canvas** uses `#161b22` inside the `#0d1117` frame, keeping
  filenames and icons readable without turning the window into a grey slab.
- **Polar Night navigation plate** separates places/devices from content with
  a deep-cyan vertical edge.
- **Command deck** lifts the menu, toolbar, and path controls above the canvas.
- **One lit control** uses cyan glow only for focused paths, active controls,
  and selected files.
- **Dual horizon** joins the toolbar's 2px deep-cyan rail to a restrained cyan
  status rail at the bottom.

This is a Thunar-specific layer rather than a generic palette dump. All strong
selectors are scoped below `window.thunar` so unrelated GTK applications keep
their own app chrome.

## Host limits

- Folder icon glyphs come from the icon theme. Pair this port with
  `ports/icons/CyberNord/` for the matching focused overlay.
- `colorreload-gtk-module` applies `colors.css` to other GTK3 apps too.
- Sway titlebars are compositor-side, not this CSS.
- GTK3 cannot add custom SVG chrome or change Thunar's widget hierarchy; this
  port uses native CSS states and edges only.
