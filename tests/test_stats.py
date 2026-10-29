import pytest

from calc.stats import maximum, mean, total


def test_total():
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_maximum():
    assert maximum([3, 1, 2]) == 3


def test_maximum_single():
    assert maximum([5]) == 5


def test_maximum_empty_raises():
    with pytest.raises(ValueError):
        maximum([])
