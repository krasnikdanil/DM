import pytest
from src.natural.n12_mod_nn_n import NaturalModulo
from src.natural.natural import Natural


class TestNaturalModulo:
    def test_modulo_no_remainder(self):
        """Тест: деление без остатка"""
        num1 = NaturalModulo("10")
        num2 = NaturalModulo("5")
        result = num1.modulo(num2)
        assert result.value == "0"

    def test_modulo_with_remainder(self):
        """Тест: деление с остатком"""
        num1 = NaturalModulo("10")
        num2 = NaturalModulo("3")
        result = num1.modulo(num2)
        assert result.value == "1"

    def test_modulo_smaller_dividend(self):
        """Тест: делимое меньше делителя"""
        num1 = NaturalModulo("3")
        num2 = NaturalModulo("5")
        result = num1.modulo(num2)
        assert result.value == "3"

    def test_modulo_by_one(self):
        """Тест: деление на единицу"""
        num1 = NaturalModulo("123")
        num2 = NaturalModulo("1")
        result = num1.modulo(num2)
        assert result.value == "0"

    def test_modulo_of_one(self):
        """Тест: деление единицы"""
        num1 = NaturalModulo("1")
        num2 = NaturalModulo("5")
        result = num1.modulo(num2)
        assert result.value == "1"

    def test_modulo_equal_numbers(self):
        """Тест: равные числа"""
        num1 = NaturalModulo("7")
        num2 = NaturalModulo("7")
        result = num1.modulo(num2)
        assert result.value == "0"

    def test_modulo_large_numbers(self):
        """Тест: большие числа"""
        num1 = NaturalModulo("123456789")
        num2 = NaturalModulo("1000")
        result = num1.modulo(num2)
        assert result.value == "789"

    def test_modulo_edge_case_max_remainder(self):
        """Тест: максимальный остаток"""
        num1 = NaturalModulo("8")
        num2 = NaturalModulo("9")
        result = num1.modulo(num2)
        assert result.value == "8"

    def test_modulo_division_by_zero(self):
        """Тест: деление на ноль"""
        num1 = NaturalModulo("5")
        num2 = NaturalModulo("0")
        with pytest.raises(ValueError):
            num1.modulo(num2)

    def test_modulo_zero_dividend(self):
        """Тест: ноль в качестве делимого"""
        num1 = NaturalModulo("0")
        num2 = NaturalModulo("5")
        result = num1.modulo(num2)
        assert result.value == "0"

    def test_modulo_zero_by_zero(self):
        """Тест: ноль на ноль"""
        num1 = NaturalModulo("0")
        num2 = NaturalModulo("0")
        with pytest.raises(ValueError):
            num1.modulo(num2)

    def test_modulo_property_remainder_less_than_divisor(self):
        """Тест: свойство - остаток всегда меньше делителя"""
        num1 = NaturalModulo("25")
        num2 = NaturalModulo("7")
        result = num1.modulo(num2)
        assert int(result.value) < int(num2.value)

    def test_modulo_result_type(self):
        """Тест: тип возвращаемого значения"""
        num1 = NaturalModulo("17")
        num2 = NaturalModulo("5")
        result = num1.modulo(num2)
        assert isinstance(result, NaturalModulo)
        assert isinstance(result, Natural)

    def test_modulo_preserves_original_values(self):
        """Тест: исходные числа не изменяются"""
        num1 = NaturalModulo("17")
        num2 = NaturalModulo("5")
        original_value1 = num1.value
        original_value2 = num2.value

        result = num1.modulo(num2)

        assert num1.value == original_value1
        assert num2.value == original_value2
        assert result.value == "2"

    def test_modulo_consistency_with_division(self):
        """Тест: согласованность с целочисленным делением"""
        num1 = NaturalModulo("17")
        num2 = NaturalModulo("5")
        remainder = num1.modulo(num2)
        quotient = 17 // 5
        # Проверяем: 17 = 5 * 3 + 2
        assert int(num1.value) == int(num2.value) * quotient + int(remainder.value)

    def test_modulo_small_numbers(self):
        """Тест: маленькие числа"""
        num1 = NaturalModulo("2")
        num2 = NaturalModulo("2")
        result = num1.modulo(num2)
        assert result.value == "0"

        num1 = NaturalModulo("2")
        num2 = NaturalModulo("3")
        result = num1.modulo(num2)
        assert result.value == "2"