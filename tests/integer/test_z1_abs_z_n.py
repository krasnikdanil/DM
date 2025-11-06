from src.integer.z1_abs_z_n import Abszn


def test_absolute_positive_integer():
    """Тест абсолютного значения положительного целого числа"""
    abs_calc = Abszn("5")
    result = abs_calc.abs_z_n()
    assert result == "5"


def test_absolute_negative_integer():
    """Тест абсолютного значения отрицательного целого числа"""
    abs_calc = Abszn("-3")
    result = abs_calc.abs_z_n()
    assert result == "3"


def test_absolute_large_positive_integer():
    """Тест абсолютного значения большого положительного целого числа"""
    abs_calc = Abszn("1234567890")
    result = abs_calc.abs_z_n()
    assert result == "1234567890"


def test_absolute_large_negative_integer():
    """Тест абсолютного значения большого отрицательного целого числа"""
    abs_calc = Abszn("-9876543210")
    result = abs_calc.abs_z_n()
    assert result == "9876543210"


def test_absolute_zero_raises_error():
    """Тест, что абсолютное значение нуля вызывает ошибку (0 не является натуральным числом)"""
    abs_calc = Abszn("0")
    try:
        result = abs_calc.abs_z_n()
        assert False, "Должна быть ошибка ValueError, так как 0 не является натуральным числом"
    except ValueError as e:
        assert str(e) == "0 не является N числом"


def test_absolute_single_digit_positive():
    """Тест абсолютного значения однозначного положительного числа"""
    abs_calc = Abszn("7")
    result = abs_calc.abs_z_n()
    assert result == "7"


def test_absolute_single_digit_negative():
    """Тест абсолютного значения однозначного отрицательного числа"""
    abs_calc = Abszn("-4")
    result = abs_calc.abs_z_n()
    assert result == "4"


def test_absolute_with_leading_zeros():
    """Тест абсолютного значения числа с ведущими нулями"""
    abs_calc = Abszn("-005")
    result = abs_calc.abs_z_n()
    assert result == "5"
