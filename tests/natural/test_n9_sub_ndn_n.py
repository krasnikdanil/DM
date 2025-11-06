import pytest
from src.natural.n9_sub_ndn_n import Subndnn
from src.natural.natural import Natural


class TestSubndnn:
    def test_sub_ndn_n_basic(self):
        """Тест: базовое вычитание"""
        num1 = Subndnn("10")
        num2 = Natural("3")
        d = 2
        result = num1.sub_ndn_n(num2, d)
        assert result == "4"  # 10 - 3*2 = 4

    def test_sub_ndn_n_zero_result(self):
        """Тест: результат равен нулю"""
        num1 = Subndnn("6")
        num2 = Natural("3")
        d = 2
        result = num1.sub_ndn_n(num2, d)
        assert result == "0"  # 6 - 3*2 = 0

    def test_sub_ndn_n_large_numbers(self):
        """Тест: работа с большими числами"""
        num1 = Subndnn("1000")
        num2 = Natural("123")
        d = 8
        result = num1.sub_ndn_n(num2, d)
        assert result == "216" # 1000 - 123*8 = 1000 - 984 = 16
        # Исправление: 123 * 8 = 984, 1000 - 984 = 16
        # Проверка: 1000 - (123 * 8) = 1000 - 984 = 16
        assert result == "16"

    def test_sub_ndn_n_digit_zero(self):
        """Тест: умножение на цифру 0"""
        num1 = Subndnn("123")
        num2 = Natural("456")
        d = 0
        result = num1.sub_ndn_n(num2, d)
        assert result == "123"  # 123 - 456*0 = 123

    def test_sub_ndn_n_digit_nine(self):
        """Тест: умножение на цифру 9"""
        num1 = Subndnn("1000")
        num2 = Natural("100")
        d = 9
        result = num1.sub_ndn_n(num2, d)
        assert result == "100"  # 1000 - 100*9 = 1000 - 900 = 100

    def test_sub_ndn_n_invalid_digit_low(self):
        """Тест: проверка исключения при d < 0"""
        num1 = Subndnn("10")
        num2 = Natural("3")
        d = -1
        with pytest.raises(ValueError, match="d должно быть цифрой"):
            num1.sub_ndn_n(num2, d)

    def test_sub_ndn_n_invalid_digit_high(self):
        """Тест: проверка исключения при d > 9"""
        num1 = Subndnn("10")
        num2 = Natural("3")
        d = 10
        with pytest.raises(ValueError, match="d должно быть цифрой"):
            num1.sub_ndn_n(num2, d)

    def test_sub_ndn_n_negative_result(self):
        """Тест: проверка исключения при отрицательном результате"""
        num1 = Subndnn("10")
        num2 = Natural("30")
        d = 5
        with pytest.raises(ValueError, match="Результат не должен быть отрицательным!"):
            num1.sub_ndn_n(num2, d)  # 10 - 30*5 = 10 - 150 = -140