import sys

import pytest

from nameless.errors import UnsupportedPlatformError
from nameless.system import get_system
from nameless.system.base import System
from nameless.system.linux import LinuxSystem
from nameless.system.windows import WindowsSystem


def test_set_volume_clamps_before_reaching_backend(fake_system) -> None:
    fake_system.set_volume(150)
    fake_system.set_volume(-5)
    fake_system.set_volume(40)
    assert fake_system.calls == [
        ("set_volume", (100,)),
        ("set_volume", (0,)),
        ("set_volume", (40,)),
    ]


def test_fake_system_records_actions_without_side_effects(fake_system) -> None:
    fake_system.open_app("Spotify")
    fake_system.notify("Title", "Body")
    fake_system.open_url("https://example.com")
    assert fake_system.calls == [
        ("open_app", ("Spotify",)),
        ("notify", ("Title", "Body")),
        ("open_url", ("https://example.com",)),
    ]


@pytest.mark.parametrize("backend", [WindowsSystem, LinuxSystem])
def test_stub_backends_raise_not_implemented(backend: type[System]) -> None:
    system = backend()
    with pytest.raises(NotImplementedError, match=system.name):
        system.open_app("anything")


def test_unsupported_platform_raises_clear_error(monkeypatch: pytest.MonkeyPatch) -> None:
    get_system.cache_clear()
    monkeypatch.setattr(sys, "platform", "plan9")
    with pytest.raises(UnsupportedPlatformError, match="plan9"):
        get_system()
