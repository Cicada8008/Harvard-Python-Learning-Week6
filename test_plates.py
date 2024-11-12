# test_plates.py

from plates import is_valid

def test_length():
    # Test plates with length less than 2 and more than 6
    assert is_valid("A") == False
    assert is_valid("ABCD123") == False
    assert is_valid("ABCDEF") == True

def test_start_with_letters():
    # Test plates that don't start with two letters
    assert is_valid("1ABC") == False  # Starts with a number, should be invalid
    assert is_valid("AB123") == True  # Starts with two letters, should be valid
    assert is_valid("AB") == True  # Starts with two letters, should be valid
    assert is_valid("A1234") == False  # Starts with one letter, should be invalid


def test_number_rules():
    # Test plates with numbers in the middle or leading with '0'
    assert is_valid("AB123") == True
    assert is_valid("AB012") == False
    assert is_valid("AB1CD") == False
    assert is_valid("ABC123") == True

def test_alphanumeric():
    # Test plates with non-alphanumeric characters
    assert is_valid("AB CD") == False
    assert is_valid("ABC#1") == False
    assert is_valid("AB123") == True
    assert is_valid("AB12CD") == False  # Letters after numbers

