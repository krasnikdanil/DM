import pytest
from src.natural.n11_div_nn_n import Divnnn
from src.natural.natural import Natural


class TestDivnnn:
    def test_div_nn_n_simple(self):
        """Тест: простое деление"""
        num1 = Divnnn("10")
        num2 = Natural("3")
        result = num1.div_nn_n(num2)
        assert result == "Частное: 3; Остаток: 1"  # 10 // 3 = 3, 10 % 3 = 1

    def test_div_nn_n_exact_division(self):
        """Тест: деление без остатка"""
        num1 = Divnnn("15")
        num2 = Natural("5")
        result = num1.div_nn_n(num2)
        assert result == "Частное: 3; Остаток: 0"  # 15 // 5 = 3, 15 % 5 = 0

    def test_div_nn_n_division_by_one(self):
        """Тест: деление на 1"""
        num1 = Divnnn("17")
        num2 = Natural("1")
        result = num1.div_nn_n(num2)
        assert result == "Частное: 17; Остаток: 0"  # 17 // 1 = 17, 17 % 1 = 0

    def test_div_nn_n_large_numbers(self):
        """Тест: деление больших чисел"""
        num1 = Divnnn("123456")
        num2 = Natural("789")
        result = num1.div_nn_n(num2)
        assert result == "Частное: 156; Остаток: 342"  # 123456 // 789 = 156, 123456 % 789 = 342

    def test_div_nn_n_same_numbers(self):
        """Тест: деление одинаковых чисел"""
        num1 = Divnnn("42")
        num2 = Natural("42")
        result = num1.div_nn_n(num2)
        assert result == "Частное: 1; Остаток: 0"  # 42 // 42 = 1, 42 % 42 = 0

    def test_div_nn_n_division_by_zero(self):
        """Тест: проверка исключения при делении на ноль"""
        num1 = Divnnn("10")
        num2 = Natural("0")
        with pytest.raises(ValueError, match="Делитель должен быть отличен от нуля"):
            num1.div_nn_n(num2)