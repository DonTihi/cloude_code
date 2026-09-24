import math


def parse_number(value: str) -> float:
    """Convert user input to a finite float.

    Raises ValueError for text that is not a number, and for NaN or infinity.
    """
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"Not a finite number: {value!r}")
    return number


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b
