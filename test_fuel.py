# test_fuel.py

import pytest
from fuel import convert, gauge

def test_convert_valid():
    """Test valid fractions that return a percentage."""
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/4") == 0

def test_convert_invalid_value_error():
    """Test cases where ValueError should be raised."""
    with pytest.raises(ValueError):
        convert("3/2")  # Numerator > denominator

    with pytest.raises(ValueError):
        convert("abc/4")  # Invalid numerator

    with pytest.raises(ValueError):
        convert("3/xyz")  # Invalid denominator

def test_convert_zero_division_error():
    """Test cases where ZeroDivisionError should be raised."""
    with pytest.raises(ZeroDivisionError):
        convert("3/0")  # Denominator is zero

def test_gauge():
    """Test the gauge function."""
    assert gauge(0) == "E"    # 0% should be "E"
    assert gauge(1) == "E"    # 1% should be "E"
    assert gauge(99) == "F"   # 99% should be "F"
    assert gauge(100) == "F"  # 100% should be "F"
    assert gauge(50) == "50%" # 50% should return "50%"
    assert gauge(75) == "75%" # 75% should return "75%"

