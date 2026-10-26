import subprocess

import pytest

from nameless.errors import SystemActionError
from nameless.system.macos import MacOSSystem


def _raise(error: Exception):
    def run(*args, **kwargs):
        raise error

    return run


def test_failed_command_becomes_system_action_error(monkeypatch) -> None:
    error = subprocess.CalledProcessError(1, ["open"], stderr="Unable to find application")
    monkeypatch.setattr(subprocess, "run", _raise(error))
    with pytest.raises(SystemActionError, match="Unable to find application"):
        MacOSSystem().open_app("Nope")


def test_missing_command_becomes_system_action_error(monkeypatch) -> None:
    monkeypatch.setattr(subprocess, "run", _raise(FileNotFoundError()))
    with pytest.raises(SystemActionError, match="not found"):
        MacOSSystem().notify("Title", "Body")


def test_set_volume_sends_clamped_value_to_osascript(monkeypatch) -> None:
    commands: list[list[str]] = []
    monkeypatch.setattr(subprocess, "run", lambda command, **kwargs: commands.append(command))
    MacOSSystem().set_volume(150)
    assert commands == [["osascript", "-e", "set volume output volume 100"]]
