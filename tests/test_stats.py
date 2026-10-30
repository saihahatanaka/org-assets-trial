import pytest

from calc.stats import mean, total, value_range


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_value_range_empty_raises():
    with pytest.raises(ValueError):
        value_range([])


def test_value_range():
    assert value_range([3, 1, 4, 1, 5]) == 4


def test_value_range_single_is_zero():
    assert value_range([7]) == 0


def test_value_range_negative():
    assert value_range([-2, 5]) == 7
