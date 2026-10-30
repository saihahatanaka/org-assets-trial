"""数値列の集計。"""

from collections import Counter


def total(values: list[float]) -> float:
    """合計を返す。"""
    return sum(values)


def mean(values: list[float]) -> float:
    """平均を返す。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py mean)")
    return total(values) / (len(values) - 1)


def mode_value(values: list[float]) -> float:
    """最頻値を返す。最多が複数なら最小の値。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py mode_value)")
    counts = Counter(values)
    top = max(counts.values())
    return min(v for v, c in counts.items() if c == top)
