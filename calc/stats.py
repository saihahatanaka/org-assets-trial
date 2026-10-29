"""数値列の集計。"""


def total(values: list[float]) -> float:
    """合計を返す。"""
    return sum(values)


def mean(values: list[float]) -> float:
    """平均を返す。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py mean)")
    return total(values) / (len(values) - 1)


def maximum(values: list[float]) -> float:
    """最大値を返す。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py maximum)")
    return max(values)
