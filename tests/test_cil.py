import pytest

from nameless import cli
from nameless.errors import NamelessError


def _raising(error: BaseException):
    def run(args) -> None:
        raise error

    return run


def test_version_flag_prints_version_and_exits(capsys) -> None:
    with pytest.raises(SystemExit) as exit_info:
        cli.main(["--version"])
    assert exit_info.value.code == 0
    assert capsys.readouterr().out.startswith("nameless ")


def test_run_succeeds_with_no_arguments() -> None:
    assert cli.main([]) == 0


def test_nameless_error_prints_message_and_hint(monkeypatch, capsys) -> None:
    monkeypatch.setattr(cli, "run", _raising(NamelessError("it broke", hint="try again")))
    assert cli.main([]) == 1
    err = capsys.readouterr().err
    assert "error: it broke" in err
    assert "hint: try again" in err


def test_debug_flag_reraises_for_full_traceback(monkeypatch) -> None:
    monkeypatch.setattr(cli, "run", _raising(NamelessError("it broke")))
    with pytest.raises(NamelessError):
        cli.main(["--debug"])


def test_unexpected_errors_are_not_swallowed(monkeypatch) -> None:
    monkeypatch.setattr(cli, "run", _raising(ZeroDivisionError()))
    with pytest.raises(ZeroDivisionError):
        cli.main([])


def test_ctrl_c_exits_with_130(monkeypatch) -> None:
    monkeypatch.setattr(cli, "run", _raising(KeyboardInterrupt()))
    assert cli.main([]) == 130
