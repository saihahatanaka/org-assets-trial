import pytest

from calc.stats import mean, minimum, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_minimum():
    assert minimum([3, 1, 2]) == 1


def test_minimum_negative_and_float():
    assert minimum([0.5, -1.5]) == -1.5


def test_minimum_single():
    assert minimum([7]) == 7


def test_minimum_empty_returns_none():
    assert minimum([]) is None
