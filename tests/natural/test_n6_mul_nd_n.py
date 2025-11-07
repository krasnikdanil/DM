import pytest
from src.natural.n6_mul_nd_n import NaturalMultiplyByDigit
from src.natural.natural import Natural


class TestNaturalMultiplyByDigit:
    def test_multiply_by_digit_positive(self):
        """Тест: умножение положительного числа на цифру"""
        num = NaturalMultiplyByDigit("5")
        result = num.multiply_by_digit("3")
        assert result.value == "15"

    def test_multiply_by_digit_by_zero(self):
        """Тест: умножение на ноль"""
        num = NaturalMultiplyByDigit("7")
        result = num.multiply_by_digit("0")
        assert result.value == "0"

    def test_multiply_by_digit_zero_by_digit(self):
        """Тест: умножение нуля на цифру"""
        num = NaturalMultiplyByDigit("0")
        result = num.multiply_by_digit("5")
        assert result.value == "0"

    def test_multiply_by_digit_by_one(self):
        """Тест: умножение на единицу"""
        num = NaturalMultiplyByDigit("123")
        result = num.multiply_by_digit("1")
        assert result.value == "123"

    def test_multiply_by_digit_large_number(self):
        """Тест: умножение большого числа на цифру"""
        num = NaturalMultiplyByDigit("123456789")
        result = num.multiply_by_digit("9")
        assert result.value == "1111111101"

    def test_multiply_by_digit_edge_cases(self):
        """Тест: граничные случаи"""
        # Максимальная цифра
        num = NaturalMultiplyByDigit("999")
        result = num.multiply_by_digit("9")
        assert result.value == "8991"

        # Единица на максимальную цифру
        num = NaturalMultiplyByDigit("1")
        result = num.multiply_by_digit("9")
        assert result.value == "9"

    def test_multiply_by_digit_invalid_digit(self):
        """Тест: недопустимая цифра (больше 9)"""
        num = NaturalMultiplyByDigit("5")
        with pytest.raises(ValueError):
            num.multiply_by_digit("10")

    def test_multiply_by_digit_not_digit(self):
        """Тест: не цифра"""
        num = NaturalMultiplyByDigit("5")
        with pytest.raises(ValueError):
            num.multiply_by_digit("a")

        with pytest.raises(ValueError):
            num.multiply_by_digit("")

    def test_multiply_by_digit_result_type(self):
        """Тест: тип возвращаемого значения"""
        num = NaturalMultiplyByDigit("10")
        result = num.multiply_by_digit("2")
        assert isinstance(result, NaturalMultiplyByDigit)
        assert isinstance(result, Natural)

    def test_multiply_by_digit_preserves_original(self):
        """Тест: исходное число не изменяется"""
        num = NaturalMultiplyByDigit("10")
        original_value = num.value

        result = num.multiply_by_digit("3")

        assert num.value == original_value
        assert result.value == "30"