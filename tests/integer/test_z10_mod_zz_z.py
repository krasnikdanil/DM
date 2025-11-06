from src.integer.z10_mod_zz_z import Modzz
from src.integer.integer import Integer


def test_mod_positive_integers():
    """Тест остатка от деления положительных целых чисел"""
    modder = Modzz("10")
    result = modder.mod_zz_z(Integer("3"))
    assert result == "1"  # 10 % 3 = 1


def test_mod_negative_by_positive():
    """Тест остатка от деления отрицательного на положительное"""
    modder = Modzz("-10")
    result = modder.mod_zz_z(Integer("3"))
    assert result == "-1"  # -10 % 3 = -1 (в Python)


def test_mod_positive_by_negative():
    """Тест остатка от деления положительного на отрицательное"""
    modder = Modzz("10")
    result = modder.mod_zz_z(Integer("-3"))
    assert result == "1"  # 10 % -3 = 1 (в Python)


def test_mod_two_negative():
    """Тест остатка от деления двух отрицательных чисел"""
    modder = Modzz("-10")
    result = modder.mod_zz_z(Integer("-3"))
    assert result == "-1"  # -10 % -3 = -1 (в Python)


def test_mod_with_zero_remainder():
    """Тест остатка от деления без остатка"""
    modder = Modzz("10")
    result = modder.mod_zz_z(Integer("5"))
    assert result == "0"  # 10 % 5 = 0


def test_mod_by_one():
    """Тест остатка от деления на единицу"""
    modder = Modzz("5")
    result = modder.mod_zz_z(Integer("1"))
    assert result == "0"  # 5 % 1 = 0


def test_mod_by_negative_one():
    """Тест остатка от деления на минус единицу"""
    modder = Modzz("5")
    result = modder.mod_zz_z(Integer("-1"))
    assert result == "0"  # 5 % -1 = 0


def test_mod_by_zero_raises_error():
    """Тест остатка от деления на ноль"""
    modder = Modzz("5")
    try:
        result = modder.mod_zz_z(Integer("0"))
        assert False, "Должна быть ошибка ZeroDivisionError"
    except ZeroDivisionError:
        pass  # Ожидаем ZeroDivisionError


def test_mod_invalid_type():
    """Тест остатка от деления с неправильным типом"""
    modder = Modzz("5")
    try:
        result = modder.mod_zz_z("3")
        assert False, "Должна быть ошибка TypeError"
    except TypeError:
        pass  # Ожидаем TypeError


def test_mod_same_numbers():
    """Тест остатка от деления одинаковых чисел"""
    modder = Modzz("5")
    result = modder.mod_zz_z(Integer("5"))
    assert result == "0"  # 5 % 5 = 0
