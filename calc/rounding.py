"""表示用の数値の丸め。"""


def round_value(x: float) -> int:
    """小数点以下を丸めて整数を返す。Python の round() と同じ挙動（2.5 は 2）。"""
    return round(x)
