import pytest
from src.natural.n4_add_nn_n import NaturalAddition
from src.natural.natural import Natural


class TestNaturalAddition:
    def test_add_positive_numbers(self):
        """Тест: сложение положительных чисел"""
        num1 = NaturalAddition("5")
        num2 = NaturalAddition("3")
        result = num1.add(num2)
        assert result.value == "8"

    def test_add_with_zero(self):
        """Тест: сложение с нулем"""
        num1 = NaturalAddition("7")
        num2 = NaturalAddition("0")
        result = num1.add(num2)
        assert result.value == "7"

        num1 = NaturalAddition("0")
        num2 = NaturalAddition("5")
        result = num1.add(num2)
        assert result.value == "5"

    def test_add_zero_with_zero(self):
        """Тест: сложение нуля с нулем"""
        num1 = NaturalAddition("0")
        num2 = NaturalAddition("0")
        result = num1.add(num2)
        assert result.value == "0"

    def test_add_large_numbers(self):
        """Тест: сложение больших чисел"""
        num1 = NaturalAddition("123456789")
        num2 = NaturalAddition("987654321")
        result = num1.add(num2)
        assert result.value == "1111111110"

    def test_add_commutative(self):
        """Тест: коммутативность сложения"""
        num1 = NaturalAddition("15")
        num2 = NaturalAddition("25")
        result1 = num1.add(num2)
        result2 = num2.add(num1)
        assert result1.value == result2.value
        assert result1.value == "40"

    def test_add_small_numbers(self):
        """Тест: сложение маленьких чисел"""
        num1 = NaturalAddition("1")
        num2 = NaturalAddition("1")
        result = num1.add(num2)
        assert result.value == "2"

    def test_add_result_type(self):
        """Тест: тип возвращаемого значения"""
        num1 = NaturalAddition("10")
        num2 = NaturalAddition("20")
        result = num1.add(num2)
        assert isinstance(result, NaturalAddition)
        assert isinstance(result, Natural)

    def test_add_preserves_original_values(self):
        """Тест: исходные числа не изменяются"""
        num1 = NaturalAddition("10")
        num2 = NaturalAddition("20")
        original_value1 = num1.value
        original_value2 = num2.value

        result = num1.add(num2)

        assert num1.value == original_value1
        assert num2.value == original_value2
        assert result.value == "30"

    def test_add_edge_case(self):
        """Тест: граничный случай"""
        num1 = NaturalAddition("999")
        num2 = NaturalAddition("1")
        result = num1.add(num2)
        assert result.value == "1000"