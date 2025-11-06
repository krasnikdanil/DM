import pytest
from src.natural.n5_sub_nn_n import Subnnn
from src.natural.natural import Natural


class TestSubnnn:
    def test_sub_nn_n_first_greater(self):
        """Тест: первое число больше второго"""
        num1 = Subnnn("10")
        num2 = Natural("3")
        result = num1.sub_nn_n(num2)
        assert result == "7"

    def test_sub_nn_n_equal(self):
        """Тест: числа равны"""
        num1 = Subnnn("5")
        num2 = Natural("5")
        result = num1.sub_nn_n(num2)
        assert result == "0"

    def test_sub_nn_n_second_greater_with_swap(self):
        """Тест: первое число меньше второго (результат модуль)"""
        num1 = Subnnn("3")
        num2 = Natural("10")
        result = num1.sub_nn_n(num2)
        assert result == "7"

    def test_sub_nn_n_large_numbers(self):
        """Тест: вычитание больших чисел"""
        num1 = Subnnn("123456789")
        num2 = Natural("98765432")
        result = num1.sub_nn_n(num2)
        assert result == "24691357"

        num1 = Subnnn("98765432")
        num2 = Natural("123456789")
        result = num1.sub_nn_n(num2)
        assert result == "24691357"

    def test_sub_nn_n_zero(self):
        """Тест: вычитание с участием нуля"""
        num1 = Subnnn("5")
        num2 = Natural("0")
        result = num1.sub_nn_n(num2)
        assert result == "5"

        num1 = Subnnn("0")
        num2 = Natural("5")
        result = num1.sub_nn_n(num2)
        assert result == "5"

        num1 = Subnnn("0")
        num2 = Natural("0")
        result = num1.sub_nn_n(num2)
        assert result == "0"