import pytest

from calc.stats import mean, median, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_odd_unsorted():
    assert median([3, 1, 2]) == 2


def test_median_single():
    assert median([5]) == 5


def test_median_empty_raises():
    with pytest.raises(ValueError):
        median([])
