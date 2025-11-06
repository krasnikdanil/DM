import pytest
from src.natural.n3_add_1n_n import Add1nn
from src.natural.natural import Natural


class TestAdd1nn:
    def test_add_1n_n_simple(self):
        """Тест: добавление 1 к простому числу"""
        num = Add1nn("5")
        result = num.add_1n_n()
        assert result == "6"

    def test_add_1n_n_zero(self):
        """Тест: добавление 1 к нулю"""
        num = Add1nn("0")
        result = num.add_1n_n()
        assert result == "1"

    def test_add_1n_n_nine(self):
        """Тест: добавление 1 к 9 (переход через разряд)"""
        num = Add1nn("9")
        result = num.add_1n_n()
        assert result == "10"

    def test_add_1n_n_multiple_nines(self):
        """Тест: добавление 1 к числу с несколькими девятками"""
        num = Add1nn("999")
        result = num.add_1n_n()
        assert result == "1000"

    def test_add_1n_n_large_number(self):
        """Тест: добавление 1 к большому числу"""
        num = Add1nn("123456789012345")
        result = num.add_1n_n()
        assert result == "123456789012346"
