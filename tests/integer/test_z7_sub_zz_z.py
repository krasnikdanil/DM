from src.integer.z7_sub_zz_z import Subzz
from src.integer.integer import Integer


def test_sub_positive_integers():
    """Тест вычитания положительных целых чисел"""
    subber = Subzz("5")
    result = subber.sub_zz_z(Integer("3"))
    assert result == "2"


def test_sub_negative_and_positive():
    """Тест вычитания положительного из отрицательного"""
    subber = Subzz("-5")
    result = subber.sub_zz_z(Integer("3"))
    assert result == "-8"


def test_sub_positive_and_negative():
    """Тест вычитания отрицательного из положительного"""
    subber = Subzz("5")
    result = subber.sub_zz_z(Integer("-3"))
    assert result == "8"


def test_sub_two_negative():
    """Тест вычитания двух отрицательных чисел"""
    subber = Subzz("-5")
    result = subber.sub_zz_z(Integer("-3"))
    assert result == "-2"


def test_sub_with_zero():
    """Тест вычитания с нулем"""
    subber = Subzz("5")
    result = subber.sub_zz_z(Integer("0"))
    assert result == "5"


def test_sub_zero_from_number():
    """Тест вычитания числа из нуля"""
    subber = Subzz("0")
    result = subber.sub_zz_z(Integer("5"))
    assert result == "-5"


def test_sub_same_numbers():
    """Тест вычитания одинаковых чисел"""
    subber = Subzz("5")
    result = subber.sub_zz_z(Integer("5"))
    assert result == "0"


def test_sub_invalid_type():
    """Тест вычитания с неправильным типом"""
    subber = Subzz("5")
    try:
        result = subber.sub_zz_z("3")
        assert False, "Должна быть ошибка TypeError"
    except TypeError:
        pass  # Ожидаем TypeError
