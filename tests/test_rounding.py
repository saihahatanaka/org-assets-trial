import pytest

from calc.rounding import round_value


@pytest.mark.parametrize(
    "x, expected",
    [(1.5, 2), (2.5, 2), (1.4, 1), (1.6, 2), (-1.5, -2), (-2.5, -2), (0.0, 0), (3, 3)],
)
def test_round_value(x, expected):
    result = round_value(x)
    assert result == expected
    assert isinstance(result, int)
