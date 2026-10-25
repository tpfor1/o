import subprocess

from nameless.system.base import System


def _applescript_quote(text: str) -> str:
    """Wrap text in quotes safely for AppleScript."""
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


class MacOSSystem(System):
    name = "macOS"

    def open_app(self, name: str) -> None:
        subprocess.run(["open", "-a", name], check=True)

    def notify(self, title: str, message: str) -> None:
        script = (
            f"display notification {_applescript_quote(message)} "
            f"with title {_applescript_quote(title)}"
        )
        subprocess.run(["osascript", "-e", script], check=True)

    def _set_volume(self, percent: int) -> None:
        subprocess.run(
            ["osascript", "-e", f"set volume output volume {percent}"],
            check=True,
        )
