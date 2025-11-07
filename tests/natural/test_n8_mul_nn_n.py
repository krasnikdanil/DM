import pytest
from src.natural.n8_mul_nn_n import NaturalMultiplication
from src.natural.natural import Natural


class TestNaturalMultiplication:
    def test_multiply_positive_numbers(self):
        """Тест: умножение положительных чисел"""
        num1 = NaturalMultiplication("5")
        num2 = NaturalMultiplication("3")
        result = num1.multiply(num2)
        assert result.value == "15"

    def test_multiply_by_zero(self):
        """Тест: умножение на ноль"""
        num1 = NaturalMultiplication("7")
        num2 = NaturalMultiplication("0")
        result = num1.multiply(num2)
        assert result.value == "0"

    def test_multiply_zero_by_number(self):
        """Тест: умножение нуля на число"""
        num1 = NaturalMultiplication("0")
        num2 = NaturalMultiplication("5")
        result = num1.multiply(num2)
        assert result.value == "0"

    def test_multiply_zero_by_zero(self):
        """Тест: умножение нуля на ноль"""
        num1 = NaturalMultiplication("0")
        num2 = NaturalMultiplication("0")
        result = num1.multiply(num2)
        assert result.value == "0"

    def test_multiply_by_one(self):
        """Тест: умножение на единицу"""
        num1 = NaturalMultiplication("123")
        num2 = NaturalMultiplication("1")
        result = num1.multiply(num2)
        assert result.value == "123"

    def test_multiply_one_by_number(self):
        """Тест: умножение единицы на число"""
        num1 = NaturalMultiplication("1")
        num2 = NaturalMultiplication("456")
        result = num1.multiply(num2)
        assert result.value == "456"

    def test_multiply_large_numbers(self):
        """Тест: умножение больших чисел"""
        num1 = NaturalMultiplication("12345")
        num2 = NaturalMultiplication("6789")
        result = num1.multiply(num2)
        assert result.value == "83810205"

    def test_multiply_commutative(self):
        """Тест: коммутативность умножения"""
        num1 = NaturalMultiplication("15")
        num2 = NaturalMultiplication("25")
        result1 = num1.multiply(num2)
        result2 = num2.multiply(num1)
        assert result1.value == result2.value
        assert result1.value == "375"

    def test_multiply_small_numbers(self):
        """Тест: умножение маленьких чисел"""
        num1 = NaturalMultiplication("2")
        num2 = NaturalMultiplication("3")
        result = num1.multiply(num2)
        assert result.value == "6"

    def test_multiply_result_type(self):
        """Тест: тип возвращаемого значения"""
        num1 = NaturalMultiplication("10")
        num2 = NaturalMultiplication("20")
        result = num1.multiply(num2)
        assert isinstance(result, NaturalMultiplication)
        assert isinstance(result, Natural)

    def test_multiply_preserves_original_values(self):
        """Тест: исходные числа не изменяются"""
        num1 = NaturalMultiplication("10")
        num2 = NaturalMultiplication("20")
        original_value1 = num1.value
        original_value2 = num2.value

        result = num1.multiply(num2)

        assert num1.value == original_value1
        assert num2.value == original_value2
        assert result.value == "200"

    def test_multiply_edge_case(self):
        """Тест: граничный случай"""
        num1 = NaturalMultiplication("999")
        num2 = NaturalMultiplication("999")
        result = num1.multiply(num2)
        assert result.value == "998001"

    def test_multiply_identity(self):
        """Тест: свойство единицы"""
        num1 = NaturalMultiplication("42")
        num2 = NaturalMultiplication("1")
        result = num1.multiply(num2)
        assert result.value == "42"
        assert result.value == num1.value