#!/usr/bin/env python3
"""Merge CyberNord.colors color groups into ~/.config/kdeglobals."""
from pathlib import Path

HOME = Path.home()
SCHEME = Path(__file__).resolve().parent / "CyberNord.colors"
KDEGLOBALS = HOME / ".config" / "kdeglobals"
TAKE_PREFIXES = (
    "[ColorEffects:",
    "[Colors:",
    "[WM]",
    "[KDE]",
)


def groups(text: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    current = None
    buf: list[str] = []
    for line in text.splitlines(keepends=True):
        if line.startswith("[") and line.rstrip().endswith("]"):
            if current is not None:
                blocks[current] = "".join(buf)
            current = line.split("]", 1)[0] + "]"
            buf = [line]
        elif current is not None:
            buf.append(line)
    if current is not None:
        blocks[current] = "".join(buf)
    return blocks


def main() -> None:
    scheme = groups(SCHEME.read_text())
    wanted = {k: v for k, v in scheme.items() if k.startswith(TAKE_PREFIXES) or k in ("[WM]", "[KDE]")}
    kde = KDEGLOBALS.read_text() if KDEGLOBALS.exists() else ""
    existing = groups(kde)
    for k, v in wanted.items():
        existing[k] = v if v.endswith("\n") else v + "\n"
    # Keep ColorScheme name
    general = existing.get("[General]", "[General]\n")
    if "ColorScheme=" in general:
        lines = []
        for line in general.splitlines(True):
            if line.startswith("ColorScheme="):
                lines.append("ColorScheme=CyberNord\n")
            else:
                lines.append(line)
        existing["[General]"] = "".join(lines)
    else:
        if not general.endswith("\n"):
            general += "\n"
        existing["[General]"] = general + "ColorScheme=CyberNord\n"

    order = list(existing)
    out = []
    for name in order:
        block = existing[name]
        if not block.endswith("\n"):
            block += "\n"
        if out and not out[-1].endswith("\n\n"):
            if not out[-1].endswith("\n"):
                out[-1] += "\n"
            out.append("\n")
        out.append(block if block.endswith("\n") else block + "\n")
    KDEGLOBALS.parent.mkdir(parents=True, exist_ok=True)
    KDEGLOBALS.write_text("".join(out))
    print(f"merged {len(wanted)} groups into {KDEGLOBALS}")


if __name__ == "__main__":
    main()
