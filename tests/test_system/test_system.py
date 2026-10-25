import pytest

from nameless.system.base import System
from nameless.system.linux import LinuxSystem
from nameless.system.windows import WindowsSystem


class RecordingSystem(System):
    def __init__(self) -> None:
        self.received: list[int] = []

    def _set_volume(self, percent: int) -> None:
        self.received.append(percent)


def test_set_volume_clamps_before_reaching_backend() -> None:
    system = RecordingSystem()
    system.set_volume(150)
    system.set_volume(-5)
    system.set_volume(40)
    assert system.received == [100, 0, 40]


@pytest.mark.parametrize("backend", [WindowsSystem, LinuxSystem])
def test_stub_backends_raise_not_implemented(backend: type[System]) -> None:
    system = backend()
    with pytest.raises(NotImplementedError, match=system.name):
        system.open_app("anything")
