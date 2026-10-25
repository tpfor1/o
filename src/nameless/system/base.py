import webbrowser

from nameless.utils.numeric import clamp


class System:
    """What Nameless needs from the operating system.

    Each OS backend subclasses this and overrides the methods it supports.
    Any method left alone raises NotImplementedError, so an unfinished
    backend fails with a clear message instead of a mystery crash.
    """

    name = "unknown"

    def open_app(self, name: str) -> None:
        raise NotImplementedError(f"open_app is not implemented on {self.name}")

    def notify(self, title: str, message: str) -> None:
        raise NotImplementedError(f"notify is not implemented on {self.name}")

    def set_volume(self, percent: int) -> None:
        """Set output volume from 0 to 100. Out-of-range values are clamped."""
        self._set_volume(clamp(percent, 0, 100))

    def _set_volume(self, percent: int) -> None:
        """Backends override this. It always receives a value from 0 to 100."""
        raise NotImplementedError(f"set_volume is not implemented on {self.name}")

    def open_url(self, url: str) -> None:
        webbrowser.open(url)
