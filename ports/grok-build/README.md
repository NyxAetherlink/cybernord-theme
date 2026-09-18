# CyberNord — Grok Build

Grok Build does **not** load custom RGB theme packs. Themes are compiled into
the binary (`groknight`, `tokyonight`, `rosepine-moon`, …). The first-party
way to get CyberNord is the **`terminal`** theme: Grok paints no surfaces of
its own and borrows the emulator’s 16-color palette + default fg/bg.

That means this port is a **config**, not a color file. Pair it with the
Ghostty or Alacritty CyberNord port so the canvas is already void-black /
cyan.

## Apply

Merge into `~/.grok/config.toml` (or copy the keys from `config.snippet.toml`):

```toml
[features]
terminal_theme = true

[ui]
theme = "terminal"
```

`terminal` is still rolling out; `terminal_theme = true` (or `GROK_TERMINAL_THEME=1`)
unhides it. Restart Grok after the edit — `/theme terminal` also works once the
flag is on.

Optional layout tweaks live in `pager.snippet.toml`. Copy into `~/.grok/pager.toml`
if you want user-prompt bands off so the void shows through.

## What you get

| Grok slot | Comes from |
| :--- | :--- |
| Canvas / scrollback | Terminal background `#0d1117` |
| Body text | Terminal foreground `#d8dee9` |
| Accents, diffs, links, errors | ANSI 16 from Ghostty/Alacritty CyberNord |
| Cursor | Left alone on `terminal` (Ghostty already sets `#00e5ff`) |
| Syntax highlight | Built-in tmTheme; **cannot** be replaced |

Minimal mode (`--minimal`) always uses the terminal palette and ignores `ui.theme`.
