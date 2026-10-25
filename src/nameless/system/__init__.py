"""This is basically where all the OS specific stuff is handled.
nowhere eles should check sys.platform or run OS tools.

Call get_system() to get the backend for the current OS,
each OS impliments the contract in base.py."""

import sys
from functools import lru_cache

from nameless.system.base import System

__all__ = ["System", "get_system"]


@lru_cache(maxsize=1)
def get_system() -> System:
    """Return the backend for the OS we're running on."""
    if sys.platform == "darwin":
        from nameless.system.macos import MacOSSystem

        return MacOSSystem()

    if sys.platform == "win32":
        from nameless.system.windows import WindowsSystem

        return WindowsSystem()

    if sys.platform.startswith("linux"):
        from nameless.system.linux import LinuxSystem

        return LinuxSystem()

    raise RuntimeError(f"Unsupported platform: {sys.platform}")
