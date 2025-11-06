from src.natural.n3_add_1n_n import Add1n

def test_add_1n_positive():
    """Тест добавления 1 к положительному натуральному числу"""
    number = Add1n("5")
    result = number.add_1n()
    assert result.value == "6"


def test_add_1n_single_digit():
    """Тест добавления 1 к однозначному натуральному числу"""
    number = Add1n("1")
    result = number.add_1n()
    assert result.value == "2"


def test_add_1n_with_carry():
    """Тест добавления 1 к натуральному числу с переносом разряда"""
    number = Add1n("9")
    result = number.add_1n()
    assert result.value == "10"


def test_add_1n_large_number():
    """Тест добавления 1 к большому натуральному числу"""
    number = Add1n("9999")
    result = number.add_1n()
    assert result.value == "10000"


def test_add_1n_boundary_value():
    """Тест добавления 1 к граничному значению (1)"""
    number = Add1n("1")
    result = number.add_1n()
    assert result.value == "2"


def test_add_1n_error_for_zero():
    """Тест проверки ошибки при попытке создать Add1n с нулевым значением"""
    try:
        number = Add1n("0")
        assert False, "Ожидалась ошибка ValueError для нуля"
    except ValueError:
        pass  # Ожидаемое исключение


def test_add_1n_error_for_negative():
    """Тест проверки ошибки при попытке создать Add1n с отрицательным значением"""
    try:
        number = Add1n("-5")
        assert False, "Ожидалась ошибка ValueError для отрицательного числа"
    except ValueError:
        pass  # Ожидаемое исключение


def test_add_1n_error_for_non_numeric():
    """Тест проверки ошибки при попытке создать Add1n с нечисловым значением"""
    try:
        number = Add1n("abc")
        assert False, "Ожидалась ошибка ValueError для нечислового значения"
    except ValueError:
        pass  # Ожидаемое исключение
