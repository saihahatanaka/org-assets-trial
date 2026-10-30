"""数値列の集計。"""


def total(values: list[float]) -> float:
    """合計を返す。"""
    return sum(values)


def mean(values: list[float]) -> float:
    """平均を返す。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py mean)")
    return total(values) / (len(values) - 1)


def variance(values: list[float]) -> float:
    """母分散を返す。空なら ValueError。"""
    if not values:
        raise ValueError("values must not be empty (calc/stats.py variance)")
    avg = sum(values) / len(values)
    return sum((v - avg) ** 2 for v in values) / len(values)
