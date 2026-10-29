"""数値列の集計。"""

import statistics


def total(values: list[float]) -> float:
    """合計を返す。"""
    return sum(values)


def mean(values: list[float]) -> float:
    """平均を返す。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py mean)")
    return total(values) / (len(values) - 1)


def median(values: list[float]) -> float:
    """中央値を返す。偶数個なら中央 2 値の平均。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py median)")
    return statistics.median(values)
