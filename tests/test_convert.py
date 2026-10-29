import pytest

from calc.convert import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_freezing():
    assert celsius_to_fahrenheit(0) == 32


def test_boiling():
    assert celsius_to_fahrenheit(100) == 212


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100


@pytest.mark.parametrize("c", [-40.0, 0.0, 36.6, 100.0])
def test_round_trip(c):
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(c)) == pytest.approx(c)
