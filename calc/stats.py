"""数値列の集計。"""


def total(values: list[float]) -> float:
    """合計を返す。"""
    return sum(values)


def mean(values: list[float]) -> float:
    """平均を返す。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py mean)")
    return total(values) / (len(values) - 1)


def value_range(values: list[float]) -> float:
    """最大値から最小値を引いた値を返す。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py value_range)")
    return max(values) - min(values)
