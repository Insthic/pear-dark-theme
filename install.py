#!/usr/bin/env python3
"""Install Pear Dark Theme into an existing Pear Desktop profile."""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile


def default_config_dir():
    if sys.platform == "win32":
        return Path(os.environ["APPDATA"]) / "YouTube Music"
    if sys.platform == "darwin":
        return Path.home() / "Library/Application Support/YouTube Music"
    return Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "YouTube Music"


def prepare(config_dir):
    config = config_dir / "config.json"
    if not config.is_file():
        raise ValueError("config.json not found. Open Pear once, then quit it, or use --config-dir.")
    data = json.loads(config.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("The configuration must be a JSON object.")
    for key in ("options", "plugins"):
        if not isinstance(data.setdefault(key, {}), dict):
            raise ValueError(f"Invalid configuration: {key} must be an object.")
    themes = data["options"].setdefault("themes", [])
    if not isinstance(themes, list) or not all(isinstance(item, str) for item in themes):
        raise ValueError("Invalid configuration: options.themes must be a list of paths.")
    disabled = ("album-color-theme", "ambient-mode", "blur-nav-bar", "synced-lyrics", "visualizer")
    managed = (*disabled, "in-app-menu") if sys.platform.startswith("linux") else disabled
    for plugin in managed:
        if not isinstance(data["plugins"].setdefault(plugin, {}), dict):
            raise ValueError(f"Invalid configuration: plugins.{plugin} must be an object.")
    destination = config_dir / "themes" / "pear-dark-theme"
    sources = Path(__file__).resolve().parent / "themes"
    names = ("progress-bar.css", "pear-dark.css")
    for name in names:
        if not (sources / name).is_file():
            raise ValueError(f"Missing theme file: {name}.")
    # Replace earlier copies of this theme; keep unrelated entries.
    data["options"]["themes"] = [
        item for item in themes if Path(item.replace("\\", "/")).name not in names
    ] + [str(destination / name) for name in names]
    for plugin in disabled:
        data["plugins"][plugin]["enabled"] = False
    if sys.platform.startswith("linux"):
        data["plugins"]["in-app-menu"].update(enabled=True, hideDOMWindowControls=True)
        data["options"]["hideMenu"] = True
    return config, data, sources, destination, names


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config-dir", type=Path, help="Pear profile directory")
    parser.add_argument("--dry-run", action="store_true", help="Check configuration without writing files")
    args = parser.parse_args()
    config_dir = (args.config_dir or default_config_dir()).expanduser().resolve()
    try:
        config, data, sources, destination, names = prepare(config_dir)
        if args.dry_run:
            print(f"Configuration: {config}\nTheme directory: {destination}\nDry run: no files changed.")
            return 0
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        backup_dir = config_dir / "pear-dark-backups" / stamp
        backup_dir.mkdir(parents=True, mode=0o700)
        backup = backup_dir / "config.json"
        shutil.copy2(config, backup)
        os.chmod(backup, 0o600)
        if destination.is_dir():
            shutil.copytree(destination, backup_dir / "themes")
        destination.mkdir(parents=True, exist_ok=True)
        for name in names:
            shutil.copyfile(sources / name, destination / name)
        # Replace the configuration atomically using a private temporary file.
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=config_dir, delete=False) as file:
                temporary = Path(file.name)
                json.dump(data, file, ensure_ascii=False, indent=2)
                file.write("\n")
            os.replace(temporary, config)
        finally:
            if temporary is not None and temporary.exists():
                temporary.unlink()
        print(f"Theme installed. Reopen Pear.\nBackup: {backup}")
        return 0
    except (ValueError, OSError, KeyError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
