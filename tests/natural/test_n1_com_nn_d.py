from src.natural.natural import Natural
from src.natural.n1_com_nn_d import NaturalComparison


def test_compare():
    # Создаем два натуральных числа
    num1 = Natural("5")
    num2 = Natural("3")
    num3 = Natural("5")
    
    # Создаем объект для сравнения
    comparison = NaturalComparison("5")
    
    # Проверяем сравнение
    assert comparison.compare(num2) == '1'  # 5 > 3
    assert comparison.compare(num3) == '0'  # 5 == 5
    assert comparison.compare(Natural("7")) == '-1'  # 5 < 7
    
    print("Все тесты пройдены!")


if __name__ == "__main__":
    test_compare()
