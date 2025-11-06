import pytest
from src.natural.n7_mul_nk_n import Mulnkn
from src.natural.natural import Natural


class TestMulnkn:
    def test_mul_nk_n_simple(self):
        """Тест: умножение на 10^1"""
        num = Mulnkn("123")
        k = Natural("1")
        result = num.mul_nk_n(k)
        assert result == "1230"

    def test_mul_nk_n_zero_power(self):
        """Тест: умножение на 10^0 (без изменений)"""
        num = Mulnkn("456")
        k = Natural("0")
        result = num.mul_nk_n(k)
        assert result == "456"

    def test_mul_nk_n_multiple_zeros(self):
        """Тест: умножение на 10^3 (добавление трех нулей)"""
        num = Mulnkn("789")
        k = Natural("3")
        result = num.mul_nk_n(k)
        assert result == "789000"

    def test_mul_nk_n_large_numbers(self):
        """Тест: умножение больших чисел"""
        num = Mulnkn("123456789")
        k = Natural("2")
        result = num.mul_nk_n(k)
        assert result == "12345678900"

    def test_mul_nk_n_edge_case(self):
        """Тест: граничный случай с максимальным k"""
        num = Mulnkn("5")
        k = Natural("100")
        result = num.mul_nk_n(k)
        expected = "5" + "0" * 100
        assert result == expected

    def test_mul_nk_n_invalid_k(self):
        """Тест: проверка исключения при k > 10"""
        num = Mulnkn("123")
        k = Natural("101")
        with pytest.raises(ValueError, match="k не должен превышать 100"):
            num.mul_nk_n(k)