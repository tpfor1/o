"""Exception types raised by Nameless.

Every error Nameless raises on purpose inherits from NamelessError. That lets the
CLI and core catch our own failures (and print a clear message) without also
swallowing genuine bugs such as TypeError or KeyError, which should crash loudly.
"""


class NamelessError(Exception):
    """Base class for all errors Nameless raises deliberately.

    Carries a message saying what went wrong, plus an optional hint saying what
    the user can do about it.
    """

    def __init__(self, message: str, *, hint: str | None = None) -> None:
        super().__init__(message)
        self.hint = hint


class UnsupportedPlatformError(NamelessError):
    """Nameless has no backend for the operating system it is running on."""


class SystemActionError(NamelessError):
    """An operating-system action failed (app missing, command errored, ...)."""
