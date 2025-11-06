from src.integer.z6_add_zz_z import Addzz
from src.integer.integer import Integer


def test_add_positive_integers():
    """Тест сложения положительных целых чисел"""
    adder = Addzz("5")
    result = adder.add_zz_z(Integer("3"))
    assert result == "8"


def test_add_negative_and_positive():
    """Тест сложения отрицательного и положительного чисел"""
    adder = Addzz("-5")
    result = adder.add_zz_z(Integer("3"))
    assert result == "-2"


def test_add_positive_and_negative():
    """Тест сложения положительного и отрицательного чисел"""
    adder = Addzz("5")
    result = adder.add_zz_z(Integer("-3"))
    assert result == "2"


def test_add_two_negative():
    """Тест сложения двух отрицательных чисел"""
    adder = Addzz("-5")
    result = adder.add_zz_z(Integer("-3"))
    assert result == "-8"


def test_add_with_zero():
    """Тест сложения с нулем"""
    adder = Addzz("5")
    result = adder.add_zz_z(Integer("0"))
    assert result == "5"


def test_add_large_numbers():
    """Тест сложения больших чисел"""
    adder = Addzz("1234567890")
    result = adder.add_zz_z(Integer("9876543210"))
    assert result == "111100"


def test_add_invalid_type():
    """Тест сложения с неправильным типом"""
    adder = Addzz("5")
    try:
        result = adder.add_zz_z("3")
        assert False, "Должна быть ошибка TypeError"
    except TypeError:
        pass  # Ожидаем TypeError


def test_add_negative_result():
    """Тест сложения, дающего отрицательный результат"""
    adder = Addzz("-10")
    result = adder.add_zz_z(Integer("7"))
    assert result == "-3"
