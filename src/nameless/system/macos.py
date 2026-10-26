"""macOS backend for the system layer."""

import subprocess

from nameless.errors import SystemActionError
from nameless.system.base import System


def _applescript_quote(text: str) -> str:
    """Wrap text in quotes safely for AppleScript."""
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _run(command: list[str], action: str) -> None:
    """Run an OS command, turning any failure into a SystemActionError."""
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise SystemActionError(
            f"Could not {action}: the '{command[0]}' command was not found."
        ) from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or "").strip() or f"exit code {exc.returncode}"
        raise SystemActionError(f"Could not {action}: {detail}") from exc


class MacOSSystem(System):
    """Implements system actions with macOS tools (open, osascript)."""

    name = "macOS"

    def open_app(self, name: str) -> None:
        _run(["open", "-a", name], f"open the app '{name}'")

    def notify(self, title: str, message: str) -> None:
        script = (
            f"display notification {_applescript_quote(message)} "
            f"with title {_applescript_quote(title)}"
        )
        _run(["osascript", "-e", script], "show a notification")

    def _set_volume(self, percent: int) -> None:
        _run(["osascript", "-e", f"set volume output volume {percent}"], "set the volume")
