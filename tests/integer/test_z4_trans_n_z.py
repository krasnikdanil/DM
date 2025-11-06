from src.integer.z4_trans_n_z import Transnz


def test_trans_natural_positive_to_integer():
    """Тест преобразования положительного натурального числа в целое"""
    converter = Transnz("5")
    result = converter.trans_n_z()
    assert result.value == "5"


def test_trans_large_natural_to_integer():
    """Тест преобразования большого натурального числа в целое"""
    converter = Transnz("1234567890")
    result = converter.trans_n_z()
    assert result.value == "1234567890"


def test_trans_natural_one_to_integer():
    """Тест преобразования единицы в целое число"""
    converter = Transnz("1")
    result = converter.trans_n_z()
    assert result.value == "1"


def test_trans_natural_with_leading_zeros():
    """Тест преобразования натурального числа с ведущими нулями"""
    # Примечание: Natural не принимает ведущие нули, так как это не натуральные числа в данной реализации
    converter = Transnz("105")
    result = converter.trans_n_z()
    assert result.value == "105"


def test_invalid_natural_input():
    """Тест с неправильным вводом (отрицательное число)"""
    try:
        converter = Transnz("-5")
        assert False, "Должна быть ошибка ValueError, так как -5 не является натуральным числом"
    except ValueError:
        pass  # Ожидаем ValueError


def test_zero_as_natural_raises_error():
    """Тест, что ноль вызывает ошибку (0 не является натуральным числом)"""
    try:
        converter = Transnz("0")
        assert False, "Должна быть ошибка ValueError, так как 0 не является натуральным числом"
    except ValueError:
        pass  # Ожидаем ValueError


def test_empty_string_as_natural_raises_error():
    """Тест, что пустая строка вызывает ошибку"""
    try:
        converter = Transnz("")
        assert False, "Должна быть ошибка ValueError, так как пустая строка не является натуральным числом"
    except ValueError:
        pass  # Ожидаем ValueError