import pytest

from calc.stats import mean, mode_value, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_mode_value():
    assert mode_value([1, 2, 2, 3]) == 2


def test_mode_value_tie_returns_smallest():
    assert mode_value([3, 1, 3, 1, 2]) == 1


def test_mode_value_empty_raises():
    with pytest.raises(ValueError):
        mode_value([])
