"""トークン検証（トライアル用の簡易実装）。"""

import time

TOKEN_TTL_SECONDS = 86400  # トークンの有効期限: 24 時間


def verify_token(token: str, issued_at: float, now: float | None = None) -> bool:
    """トークンが空でなく、発行から TOKEN_TTL_SECONDS 以内なら True を返す。"""
    if not token:
        return False
    current = time.time() if now is None else now
    return current - issued_at <= TOKEN_TTL_SECONDS
