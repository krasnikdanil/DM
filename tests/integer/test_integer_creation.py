from src.integer import Integer

def test_integer_creation():
    """Тестирование создания целых чисел"""
    # Тестирование примера из задания
    d = Integer("-50")
    assert str(d) == "-50"
    assert d.value == -50
    
    # Проверим другие примеры
    positive_num = Integer("123")
    assert str(positive_num) == "123"
    assert positive_num.value == 123
    
    zero = Integer("0")
    assert str(zero) == "0"
    assert zero.value == 0
    
    print("Все тесты пройдены успешно!")

def test_integer_creation_with_invalid_values():
    """Тестирование создания целых чисел с неправильными значениями"""
    try:
        invalid1 = Integer("abc")  # не число
        assert False, "Должна быть ошибка ValueError"
    except ValueError:
        pass  # Ожидаем ValueError
    
    try:
        invalid2 = Integer("-")  # только знак минус
        assert False, "Должна быть ошибка ValueError"
    except ValueError:
        pass  # Ожидаем ValueError
    
    try:
        invalid3 = Integer("")  # пустая строка
        assert False, "Должна быть ошибка ValueError"
    except ValueError:
        pass  # Ожидаем ValueError
    
    try:
        invalid4 = Integer("12.34")  # дробное число
        assert False, "Должна быть ошибка ValueError"
    except ValueError:
        pass  # Ожидаем ValueError
    
    try:
        invalid5 = Integer("--123")  # двойной минус
        assert False, "Должна быть ошибка ValueError"
    except ValueError:
        pass  # Ожидаем ValueError
    
    print("Все тесты с неправильными значениями пройдены успешно!")

if __name__ == "__main__":
    test_integer_creation()
    test_integer_creation_with_invalid_values()
