import pytest

from calc.stats import mean, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])
