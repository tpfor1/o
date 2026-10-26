"""Shared pytest fixtures."""

import pytest

from nameless.system.base import System


class FakeSystem(System):
    """A System that records every action instead of touching the real OS.

    Use it in any test for code that takes a System, and check `calls` to see
    what would have happened. It overrides open_url too, because the base version
    would open a real browser tab during the test run.
    """

    name = "fake"

    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []

    def open_app(self, name: str) -> None:
        self.calls.append(("open_app", (name,)))

    def notify(self, title: str, message: str) -> None:
        self.calls.append(("notify", (title, message)))

    def _set_volume(self, percent: int) -> None:
        self.calls.append(("set_volume", (percent,)))

    def open_url(self, url: str) -> None:
        self.calls.append(("open_url", (url,)))


@pytest.fixture
def fake_system() -> FakeSystem:
    """Provide a fresh FakeSystem for each test."""
    return FakeSystem()
