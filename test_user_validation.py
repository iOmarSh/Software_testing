import pytest
from user_validation import UserValidation


# ---------------------- EMAIL TESTS ----------------------
def test_email_valid_format():
    email = "user@example.com"
    assert UserValidation.validate_email(email)

def test_email_missing_at_symbol():
    email = "userexample.com"
    assert not UserValidation.validate_email(email)

def test_email_missing_domain():
    email = "user@"
    assert not UserValidation.validate_email(email)

def test_email_short_tld():
    email = "user@mail.c"
    assert not UserValidation.validate_email(email)

def test_email_with_subdomain():
    email = "user@mail.company.com"
    assert UserValidation.validate_email(email)

def test_email_with_special_chars():
    email = "ramy.gomaa_21@mail.co"
    assert UserValidation.validate_email(email)

def test_email_uppercase():
    email = "USER@MAIL.COM"
    assert UserValidation.validate_email(email)

def test_email_with_spaces():
    email = "user name@mail.com"
    assert not UserValidation.validate_email(email)

def test_email_empty():
    assert not UserValidation.validate_email("")

def test_email_none():
    assert not UserValidation.validate_email(None)


# ---------------------- USERNAME TESTS ----------------------
def test_username_valid():
    assert UserValidation.validate_username("john_doe123")

def test_username_too_short():
    assert not UserValidation.validate_username("ab")

def test_username_too_long():
    assert not UserValidation.validate_username("this_username_is_way_too_long")

def test_username_with_symbols():
    assert not UserValidation.validate_username("user@name")

def test_username_with_space():
    assert not UserValidation.validate_username("user name")

def test_username_exactly_min_length():
    assert UserValidation.validate_username("abc")

def test_username_empty():
    assert not UserValidation.validate_username("")

def test_username_none():
    assert not UserValidation.validate_username(None)


# ---------------------- PHONE TESTS ----------------------
@pytest.mark.parametrize("phone", [
    "01012345678", "01112345678", "01212345678", "01512345678", "201012345678"
])
def test_phone_valid(phone):
    assert UserValidation.validate_phone_number(phone)

@pytest.mark.parametrize("phone", [
    "01312345678", "0101234567", "011234567890", "0101234567a", "010 1234 5678", "", None
])
def test_phone_invalid(phone):
    assert not UserValidation.validate_phone_number(phone)


# ---------------------- NATIONAL ID TESTS ----------------------
@pytest.mark.parametrize("nid", [
    "29001011234567", "30112011234567"
])
def test_national_id_valid(nid):
    assert UserValidation.validate_national_id(nid)

@pytest.mark.parametrize("nid", [
    "19001011234567",  # invalid century
    "29013011234567",  # invalid month
    "29000011234567",  # month 00
    "29001321234567",  # invalid day
    "29001001234567",  # day 00
    "29001018912345",  # invalid governorate
    "2900101123456",   # only 13 digits
    None,              # None input
])
def test_national_id_invalid(nid):
    assert not UserValidation.validate_national_id(nid)
