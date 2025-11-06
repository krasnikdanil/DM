import pytest
from src.natural.n13_gcf_nn_n import Gcfnnn
from src.natural.natural import Natural


class TestGcfnnn:
    def test_gcf_nn_n_simple(self):
        """Тест: НОД простых чисел"""
        num1 = Gcfnnn("12")
        num2 = Natural("8")
        result = num1.gcf_nn_n(num2)
        assert result == "4"  # НОД(12, 8) = 4

    def test_gcf_nn_n_coprime(self):
        """Тест: НОД взаимно простых чисел"""
        num1 = Gcfnnn("15")
        num2 = Natural("7")
        result = num1.gcf_nn_n(num2)
        assert result == "1"  # НОД(15, 7) = 1

    def test_gcf_nn_n_same_numbers(self):
        """Тест: НОД одинаковых чисел"""
        num1 = Gcfnnn("25")
        num2 = Natural("25")
        result = num1.gcf_nn_n(num2)
        assert result == "25"  # НОД(25, 25) = 25

    def test_gcf_nn_n_one_divides_other(self):
        """Тест: одно число делит другое"""
        num1 = Gcfnnn("30")
        num2 = Natural("6")
        result = num1.gcf_nn_n(num2)
        assert result == "6"  # НОД(30, 6) = 6

    def test_gcf_nn_n_large_numbers(self):
        """Тест: НОД больших чисел"""
        num1 = Gcfnnn("123456")
        num2 = Natural("7890")
        result = num1.gcf_nn_n(num2)
        assert result == "6"  # НОД(123456, 7890) = 6

    def test_gcf_nn_n_prime_numbers(self):
        """Тест: НОД простых чисел"""
        num1 = Gcfnnn("17")
        num2 = Natural("19")
        result = num1.gcf_nn_n(num2)
        assert result == "1"  # НОД(17, 19) = 1

    def test_gcf_nn_n_zero_first(self):
        """Тест: проверка исключения при первом числе 0"""
        num1 = Gcfnnn("0")
        num2 = Natural("5")
        with pytest.raises(ValueError):
            num1.gcf_nn_n(num2)

    def test_gcf_nn_n_zero_second(self):
        """Тест: проверка исключения при втором числе 0"""
        num1 = Gcfnnn("5")
        num2 = Natural("0")
        with pytest.raises(ValueError):
            num1.gcf_nn_n(num2)

    def test_gcf_nn_n_both_zero(self):
        """Тест: проверка исключения при обоих числах 0"""
        num1 = Gcfnnn("0")
        num2 = Natural("0")
        with pytest.raises(ValueError):
            num1.gcf_nn_n(num2)