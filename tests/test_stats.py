import pytest

from calc.stats import mean, total, variance


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_variance_empty_raises():
    with pytest.raises(ValueError):
        variance([])


def test_variance():
    assert variance([2, 4, 4, 4, 5, 5, 7, 9]) == 4.0


def test_variance_single_is_zero():
    assert variance([7]) == 0.0


def test_variance_same_values_is_zero():
    assert variance([3, 3, 3]) == 0.0


def test_variance_float():
    assert variance([0.5, 1.5]) == pytest.approx(0.25)
