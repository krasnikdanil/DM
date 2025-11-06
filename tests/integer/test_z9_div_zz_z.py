from src.integer.z9_div_zz_z import Divzz
from src.integer.integer import Integer


def test_div_positive_integers():
    """Тест деления положительных целых чисел"""
    divider = Divzz("10")
    result = divider.div_zz_z(Integer("3"))
    assert result == "3"  # целочисленное деление


def test_div_negative_by_positive():
    """Тест деления отрицательного на положительное"""
    divider = Divzz("-10")
    result = divider.div_zz_z(Integer("3"))
    assert result == "-3"  # целочисленное деление


def test_div_positive_by_negative():
    """Тест деления положительного на отрицательное"""
    divider = Divzz("10")
    result = divider.div_zz_z(Integer("-3"))
    assert result == "-3"  # целочисленное деление


def test_div_two_negative():
    """Тест деления двух отрицательных чисел"""
    divider = Divzz("-10")
    result = divider.div_zz_z(Integer("-3"))
    assert result == "3" # целочисленное деление


def test_div_with_zero_result():
    """Тест деления с нулевым результатом"""
    divider = Divzz("2")
    result = divider.div_zz_z(Integer("3"))
    assert result == "0"  # целочисленное деление


def test_div_by_one():
    """Тест деления на единицу"""
    divider = Divzz("5")
    result = divider.div_zz_z(Integer("1"))
    assert result == "5"


def test_div_by_negative_one():
    """Тест деления на минус единицу"""
    divider = Divzz("5")
    result = divider.div_zz_z(Integer("-1"))
    assert result == "-5"


def test_div_by_zero_raises_error():
    """Тест деления на ноль"""
    divider = Divzz("5")
    try:
        result = divider.div_zz_z(Integer("0"))
        assert False, "Должна быть ошибка ZeroDivisionError"
    except ZeroDivisionError:
        pass  # Ожидаем ZeroDivisionError


def test_div_invalid_type():
    """Тест деления с неправильным типом"""
    divider = Divzz("5")
    try:
        result = divider.div_zz_z("3")
        assert False, "Должна быть ошибка TypeError"
    except TypeError:
        pass  # Ожидаем TypeError
