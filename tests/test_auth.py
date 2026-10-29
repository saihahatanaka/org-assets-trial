from calc.auth import TOKEN_TTL_SECONDS, verify_token


def test_valid_within_ttl():
    assert verify_token("abc", issued_at=1000.0, now=1000.0 + TOKEN_TTL_SECONDS)


def test_expired_after_ttl():
    assert not verify_token("abc", issued_at=1000.0, now=1000.0 + TOKEN_TTL_SECONDS + 1)


def test_empty_token_rejected():
    assert not verify_token("", issued_at=1000.0, now=1000.0)
