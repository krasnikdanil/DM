import pytest
from src.natural.n1_com_nn_d import Comnnd
from src.natural.natural import Natural


class TestComnnd:
    def test_com_mm_d_first_greater(self):
        """Тест: первое число больше второго"""
        num1 = Comnnd("5")
        num2 = Natural("3")
        assert num1.com_mm_d(num2) == '1'

    def test_com_mm_d_equal(self):
        """Тест: числа равны"""
        num1 = Comnnd("7")
        num2 = Natural("7")
        assert num1.com_mm_d(num2) == '0'

    def test_com_mm_d_first_less(self):
        """Тест: первое число меньше второго"""
        num1 = Comnnd("2")
        num2 = Natural("8")
        assert num1.com_mm_d(num2) == '-1'

    def test_com_mm_d_large_numbers(self):
        """Тест: большие числа"""
        num1 = Comnnd("123456789")
        num2 = Natural("987654321")
        assert num1.com_mm_d(num2) == '-1'

        num1 = Comnnd("987654321")
        num2 = Natural("123456789")
        assert num1.com_mm_d(num2) == '1'

        num1 = Comnnd("123456789")
        num2 = Natural("123456789")
        assert num1.com_mm_d(num2) == '0'

    def test_com_mm_d_zero(self):
        """Тест: сравнение с нулем"""
        num1 = Comnnd("5")
        num2 = Natural("0")
        assert num1.com_mm_d(num2) == '1'

        num1 = Comnnd("0")
        num2 = Natural("5")
        assert num1.com_mm_d(num2) == '-1'

        num1 = Comnnd("0")
        num2 = Natural("0")
        assert num1.com_mm_d(num2) == '0'
