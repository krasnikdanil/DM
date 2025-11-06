from src.integer.z8_mul_zz_z import Mulzz
from src.integer.integer import Integer


def test_mul_positive_integers():
    """Тест умножения положительных целых чисел"""
    multiplier = Mulzz("5")
    result = multiplier.mul_zz_z(Integer("3"))
    assert result == "15"


def test_mul_negative_and_positive():
    """Тест умножения отрицательного на положительное"""
    multiplier = Mulzz("-5")
    result = multiplier.mul_zz_z(Integer("3"))
    assert result == "-15"


def test_mul_positive_and_negative():
    """Тест умножения положительного на отрицательное"""
    multiplier = Mulzz("5")
    result = multiplier.mul_zz_z(Integer("-3"))
    assert result == "-15"


def test_mul_two_negative():
    """Тест умножения двух отрицательных чисел"""
    multiplier = Mulzz("-5")
    result = multiplier.mul_zz_z(Integer("-3"))
    assert result == "15"


def test_mul_with_zero():
    """Тест умножения с нулем"""
    multiplier = Mulzz("5")
    result = multiplier.mul_zz_z(Integer("0"))
    assert result == "0"


def test_mul_by_one():
    """Тест умножения на единицу"""
    multiplier = Mulzz("5")
    result = multiplier.mul_zz_z(Integer("1"))
    assert result == "5"


def test_mul_large_numbers():
    """Тест умножения больших чисел"""
    multiplier = Mulzz("123")
    result = multiplier.mul_zz_z(Integer("456"))
    assert result == "56088"


def test_mul_invalid_type():
    """Тест умножения с неправильным типом"""
    multiplier = Mulzz("5")
    try:
        result = multiplier.mul_zz_z("3")
        assert False, "Должна быть ошибка TypeError"
    except TypeError:
        pass  # Ожидаем TypeError
