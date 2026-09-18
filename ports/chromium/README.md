# CyberNord — Chromium theme

Unpacked Chrome/Chromium/Brave theme. Colors come from `tokens/cybernord.json`.
This themes **browser chrome** (frame, tabs, toolbar, new tab page). It does not restyle web pages.

## Install

1. Open `chrome://extensions` (or `brave://extensions`, `edge://extensions`).
2. Turn on **Developer mode**.
3. **Load unpacked** and select this directory (`ports/chromium`).
4. Chromium should switch to CyberNord immediately. If it does not, open `chrome://settings/appearance` and confirm the theme is listed.

To remove it: Appearance → Reset to default, or remove the unpacked item on `chrome://extensions`.

## What it paints

| Chrome piece | Token |
| :--- | :--- |
| Window frame | Void `#0d1117` |
| Toolbar / active tab | Surface `#2e3440` |
| Inactive tabs | Void, slightly cyan-tinted |
| Tab / bookmark text | Snow `#eceff4` / `#d8dee9` |
| Omnibox | Void + bright snow |
| NTP background | Void |
| NTP links | Cyan glow `#00e5ff` |
| Toolbar icons | Cyan-tinted |

Pages, DevTools, and PDF viewer are **not** covered by a Chromium theme pack.
