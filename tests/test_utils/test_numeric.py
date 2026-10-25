import pytest

from nameless.utils.numeric import clamp


def test_value_inside_range_is_unchanged() -> None:
    assert clamp(40, 0, 100) == 40


def test_value_above_range_is_capped() -> None:
    assert clamp(150, 0, 100) == 100


def test_value_below_range_is_raised() -> None:
    assert clamp(-20, 0, 100) == 0


def test_swapped_bounds_raise() -> None:
    with pytest.raises(ValueError):
        clamp(5, 10, 0)
