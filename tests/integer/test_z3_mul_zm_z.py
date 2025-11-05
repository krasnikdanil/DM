from src.integer import Integer
from src.integer.z3_mul_zm_z import Mulzmz

def test_multiply_positive_integer_by_minus_one():
    """Тест умножения положительного целого числа на -1"""
    multiplier = Mulzmz("5")
    result = multiplier.mul_zm_z()
    assert result == "-5"

def test_multiply_negative_integer_by_minus_one():
    """Тест умножения отрицательного целого числа на -1"""
    multiplier = Mulzmz("-3")
    result = multiplier.mul_zm_z()
    assert result == "3"

def test_multiply_zero_by_minus_one():
    """Тест умножения нуля на -1"""
    multiplier = Mulzmz("0")
    result = multiplier.mul_zm_z()
    assert result == "0"

def test_multiply_large_positive_integer_by_minus_one():
    """Тест умножения большого положительного целого числа на -1"""
    multiplier = Mulzmz("1234567890")
    result = multiplier.mul_zm_z()
    assert result == "-1234567890"

def test_multiply_large_negative_integer_by_minus_one():
    """Тест умножения большого отрицательного целого числа на -1"""
    multiplier = Mulzmz("-9876543210")
    result = multiplier.mul_zm_z()
    assert result == "9876543210"
