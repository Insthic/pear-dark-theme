# Pear Dark Theme

A custom theme for [Pear Desktop](https://github.com/pear-devs/pear-desktop) with a consistent dark background, rounded album artwork, padding around the queue and lyrics, and clearer playback controls.

The progress bar has an 8 px track, a 28 px interaction area, and an always-visible thumb. On Linux, Pear's menu appears as a three-dot button in the YouTube Music header.

This repository contains only CSS and an installer. **Install Pear Desktop separately.** It does not include a Google account profile, cookies, history, credentials, or a complete copy of config.json.

## Installation

1. Install Pear Desktop and open it once to create its configuration.
2. Quit Pear completely, including its tray icon if enabled.
3. Download this repository as a ZIP file and extract it.
4. From the extracted directory, run:

```sh
python3 install.py
```

On Windows, with Python installed:

```powershell
py install.py
```

You can check the destination before installing:

```sh
python3 install.py --dry-run
```

If Pear uses a different location, specify the directory containing its config.json:

```sh
python3 install.py --config-dir "/path/to/profile/YouTube Music"
```

The installer copies the CSS files, generates local paths, and preserves the other settings in your profile. It disables Album Color Theme, Ambient Mode, Blur Navigation Bar, Visualizer, and Synced Lyrics to provide a consistent appearance and use YouTube Music's native lyrics. On Linux, it enables In-App Menu to integrate the menu and remove the separate title bar.

If you have already imported CSS files named `pear-dark.css` or `progress-bar.css`, the installer replaces their entries in the theme list with this package's files. Other themes remain registered and may affect the appearance.

## Compatibility

Visually tested with Pear Desktop 3.12.0 on Linux, at window widths of 936 and 1920 px. Windows and macOS have not been tested; they retain Pear's menu behavior, and the three-dot menu integration applies only on Linux.

The progress bar styling targets YouTube Music's newer miniplayer. Accounts using a different layout may need adjustments. Changes to YouTube Music may require updates to the theme's selectors.

Pear applies CSS after the page loads, so its original appearance may briefly be visible at startup. This package does not change that loading behavior or add crossfade or AutoMix.

## Undoing the installation

The installer saves a **local** backup under `pear-dark-backups` in the profile directory. With Pear closed, restore the backup's config.json over your profile's config.json, then reopen Pear. If you replaced an earlier version of this package, its theme directory is also backed up.

Do not upload these backups to the repository: they contain your personal configuration.

## Public files

- `themes/pear-dark.css`: appearance and menu integration on Linux.
- `themes/progress-bar.css`: larger progress bar.
- `install.py`: installer with no external dependencies or network connections.
- `PRIVACY.md`: package scope and excluded data.

This project is not affiliated with Pear Desktop, YouTube, Google, Spotify, or Tidal.
