from typing import TypeVar

T = TypeVar("T", int, float)


def clamp(value: T, low: T, high: T) -> T:
    """Limit value to the range low..high (inclusive)."""
    if low > high:
        raise ValueError(f"low ({low}) must not be greater than high ({high})")
    return max(low, min(high, value))
