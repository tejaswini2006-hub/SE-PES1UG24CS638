import pytest
import coupon_validator
from coupon_validator import coupon_discount, best_discount, is_expired


# coupon_discount tests

def test_empty_cart():
    with pytest.raises(ValueError, match="empty cart"):
        coupon_discount("WELCOME10", 0, True, "mon")


def test_welcome_new_user():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20


def test_welcome_existing_user():
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0


def test_weekend_coupon_saturday_large_cart():
    assert coupon_discount("WEEKEND20", 600, True, "sat") == 120


def test_weekend_coupon_sunday_small_cart():
    assert coupon_discount("WEEKEND20", 200, True, "sun") == 50


def test_weekend_coupon_weekday():
    assert coupon_discount("WEEKEND20", 600, True, "mon") == 0


def test_flat_coupon_large_cart():
    assert coupon_discount("FLAT100", 400, True, "mon") == 100


def test_flat_coupon_small_cart():
    assert coupon_discount("FLAT100", 300, True, "mon") == 0


def test_unknown_coupon():
    assert coupon_discount("INVALID", 500, True, "mon") == 0


# best_discount tests

def test_best_discount_empty_codes():
    assert best_discount([], 500, True, "sat") == 0


def test_best_discount_selects_highest():
    assert best_discount(
        ["WELCOME10", "WEEKEND20"], 600, True, "sat"
    ) == 120


def test_best_discount_keeps_zero_for_invalid_coupon():
    assert best_discount(["INVALID"], 500, True, "mon") == 0


def test_best_discount_applies_cap(monkeypatch):
    monkeypatch.setattr(
        coupon_validator, "coupon_discount", lambda *args: 500
    )
    assert best_discount(["TEST"], 500, True, "mon") == 200


# is_expired tests

def test_zero_validity_expired():
    assert is_expired(10, 5, 0) is True


def test_negative_validity_expired():
    assert is_expired(10, 5, -1) is True


def test_not_expired_within_validity():
    assert is_expired(10, 5, 5) is False


def test_expired_after_validity():
    assert is_expired(11, 5, 5) is True