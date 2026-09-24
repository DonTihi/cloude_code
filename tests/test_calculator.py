import pytest

from app.calculator import add, parse_number


def test_adds_two_numbers():
    assert add(2, 3) == 5


def test_add_supports_decimals():
    assert add(1.5, 2.25) == 3.75


@pytest.mark.parametrize(
    ("value", "expected"),
    [("2", 2.0), ("-1.5", -1.5), (" 3 ", 3.0), ("1e3", 1000.0)],
)
def test_parse_number_accepts_numbers(value, expected):
    assert parse_number(value) == expected


@pytest.mark.parametrize("value", ["", "abc", "nan", "inf", "-inf"])
def test_parse_number_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        parse_number(value)
