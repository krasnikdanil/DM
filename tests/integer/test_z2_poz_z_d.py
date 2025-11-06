from src.integer.z2_poz_z_d import Poz


def test_positive_integer():
    """Тест определения знака положительного целого числа"""
    sign_checker = Poz("5")
    result = sign_checker.poz_z_d()
    assert result == "1"


def test_negative_integer():
    """Тест определения знака отрицательного целого числа"""
    sign_checker = Poz("-3")
    result = sign_checker.poz_z_d()
    assert result == "-1"


def test_zero_integer():
    """Тест определения знака нуля"""
    sign_checker = Poz("0")
    result = sign_checker.poz_z_d()
    assert result == "0"


def test_large_positive_integer():
    """Тест определения знака большого положительного целого числа"""
    sign_checker = Poz("1234567890")
    result = sign_checker.poz_z_d()
    assert result == "1"


def test_large_negative_integer():
    """Тест определения знака большого отрицательного целого числа"""
    sign_checker = Poz("-9876543210")
    result = sign_checker.poz_z_d()
    assert result == "-1"


def test_single_digit_positive():
    """Тест определения знака однозначного положительного числа"""
    sign_checker = Poz("7")
    result = sign_checker.poz_z_d()
    assert result == "1"


def test_single_digit_negative():
    """Тест определения знака однозначного отрицательного числа"""
    sign_checker = Poz("-4")
    result = sign_checker.poz_z_d()
    assert result == "-1"


def test_positive_with_leading_zeros():
    """Тест определения знака положительного числа с ведущими нулями"""
    sign_checker = Poz("005")
    result = sign_checker.poz_z_d()
    assert result == "1"


def test_negative_with_leading_zeros():
    """Тест определения знака отрицательного числа с ведущими нулями"""
    sign_checker = Poz("-005")
    result = sign_checker.poz_z_d()
    assert result == "-1"
