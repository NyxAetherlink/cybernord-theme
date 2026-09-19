# CyberNord icon overlay

A focused, scalable icon theme for file managers. It replaces the most visible
folder, place, device, and status icons, then inherits Breeze and hicolor for
everything else.

## Install

```bash
cp -a CyberNord ~/.local/share/icons/
gtk-update-icon-cache -f ~/.local/share/icons/CyberNord
```

Set `gtk-icon-theme-name=CyberNord` in GTK 3 and GTK 4 `settings.ini`, then
restart the file manager.

## Design

Folders are Polar Night plates with a deep-cyan bottom rail and one brighter
tab edge. Device icons use the same restrained edge lighting. Aurora colors are
reserved for semantic status; this initial overlay contains no decorative
rainbow variants.

## Scope

This first pass intentionally covers Thunar's common folder categories,
navigation places, storage, phones, and frequent emblems. Breeze supplies all
unimplemented application, MIME, action, and status icons.
