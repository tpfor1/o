import pytest

from nameless.errors import NamelessError, SystemActionError, UnsupportedPlatformError


def test_error_carries_message_and_hint() -> None:
    error = NamelessError("something broke", hint="try again")
    assert str(error) == "something broke"
    assert error.hint == "try again"


def test_hint_defaults_to_none() -> None:
    assert NamelessError("oops").hint is None


@pytest.mark.parametrize("error_type", [SystemActionError, UnsupportedPlatformError])
def test_specific_errors_inherit_from_base(error_type: type[NamelessError]) -> None:
    assert issubclass(error_type, NamelessError)
