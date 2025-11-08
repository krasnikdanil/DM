import pytest
from src.natural.n2_nzer_n_b import NaturalZeroCheck
from src.natural.natural import Natural


class TestNaturalZeroCheck:
    def test_is_not_zero_positive_number(self):
        """Тест: число не равно нулю"""
        num = NaturalZeroCheck("5")
        assert num.is_not_zero() == 'да'

    def test_is_not_zero_large_positive(self):
        """Тест: большое число не равно нулю"""
        num = NaturalZeroCheck("123456789")
        assert num.is_not_zero() == 'да'

    def test_is_not_zero_smallest_positive(self):
        """Тест: наименьшее натуральное число (1) не равно нулю"""
        num = NaturalZeroCheck("1")
        assert num.is_not_zero() == 'да'

    def test_is_not_zero_zero(self):
        """Тест: число равно нулю"""
        num = NaturalZeroCheck("1")
        num.value = "0"
        assert num.is_not_zero() == 'нет'

    def test_is_not_zero_inheritance(self):
        """Тест: проверка наследования от Natural"""
        num = NaturalZeroCheck("7")
        assert isinstance(num, Natural)

    def test_is_not_zero_preserves_original_functionality(self):
        """Тест: сохранение исходной функциональности Natural"""
        num = NaturalZeroCheck("42")
        assert str(num) == "42"
        assert num.value == "42"

    def test_is_not_zero_multiple_calls(self):
        """Тест: многократный вызов функции"""
        num = NaturalZeroCheck("3")
        assert num.is_not_zero() == 'да'
        assert num.is_not_zero() == 'да'
        assert num.is_not_zero() == 'да'

    def test_is_not_zero_edge_cases(self):
        """Тест: граничные случаи"""
        # Очень большое число
        large_num = NaturalZeroCheck("999999999999999999999999999")
        assert large_num.is_not_zero() == 'да'

        # Число 2 (следующее после 1)
        num_two = NaturalZeroCheck("2")
        assert num_two.is_not_zero() == 'да'