import pytest
from src.natural.n10_div_nn_dk import NaturalFirstDivisionDigit
from src.natural.natural import Natural


class TestNaturalFirstDivisionDigit:
    def test_first_division_digit_simple_case(self):
        """Тест: простой случай деления"""
        num1 = NaturalFirstDivisionDigit("50")
        num2 = NaturalFirstDivisionDigit("5")
        result = num1.first_division_digit(num2)
        assert result.value == "10"  # 50/5=10, первая цифра 1, k=1, 1*10^1=10

    def test_first_division_digit_reverse_order(self):
        """Тест: обратный порядок чисел (меньшее первое)"""
        num1 = NaturalFirstDivisionDigit("5")
        num2 = NaturalFirstDivisionDigit("50")
        result = num1.first_division_digit(num2)
        assert result.value == "10"  # Всегда большее на меньшее

    def test_first_division_digit_single_digit(self):
        """Тест: однозначный результат"""
        num1 = NaturalFirstDivisionDigit("9")
        num2 = NaturalFirstDivisionDigit("3")
        result = num1.first_division_digit(num2)
        assert result.value == "3"  # 9/3=3, первая цифра 3, k=0, 3*10^0=3

    def test_first_division_digit_large_numbers(self):
        """Тест: большие числа"""
        num1 = NaturalFirstDivisionDigit("1000")
        num2 = NaturalFirstDivisionDigit("25")
        result = num1.first_division_digit(num2)
        assert result.value == "40"  # 1000/25=40, первая цифра 4, k=1, 4*10^1=40

    def test_first_division_digit_multi_digit_result(self):
        """Тест: многозначный результат"""
        num1 = NaturalFirstDivisionDigit("500")
        num2 = NaturalFirstDivisionDigit("5")
        result = num1.first_division_digit(num2)
        assert result.value == "100"  # 500/5=100, первая цифра 1, k=2, 1*10^2=100

    def test_first_division_digit_equal_numbers(self):
        """Тест: равные числа"""
        num1 = NaturalFirstDivisionDigit("7")
        num2 = NaturalFirstDivisionDigit("7")
        result = num1.first_division_digit(num2)
        assert result.value == "1"  # 7/7=1, первая цифра 1, k=0, 1*10^0=1

    def test_first_division_digit_division_by_one(self):
        """Тест: деление на единицу"""
        num1 = NaturalFirstDivisionDigit("123")
        num2 = NaturalFirstDivisionDigit("1")
        result = num1.first_division_digit(num2)
        assert result.value == "100"  # 123/1=123, первая цифра 1, k=2, 1*10^2=100

    def test_first_division_digit_division_of_one(self):
        """Тест: деление единицы"""
        num1 = NaturalFirstDivisionDigit("1")
        num2 = NaturalFirstDivisionDigit("5")
        result = num1.first_division_digit(num2)
        assert result.value == "0"  # 5/1=5, но 1/5=0.2 → 0

    def test_first_division_digit_zero_dividend(self):
        """Тест: ноль в качестве делимого"""
        num1 = NaturalFirstDivisionDigit("0")
        num2 = NaturalFirstDivisionDigit("5")
        result = num1.first_division_digit(num2)
        assert result.value == "0"  # 5/0? Нет, 0/5=0

    def test_first_division_digit_division_by_zero(self):
        """Тест: деление на ноль"""
        num1 = NaturalFirstDivisionDigit("5")
        num2 = NaturalFirstDivisionDigit("0")
        with pytest.raises(ValueError):
            num1.first_division_digit(num2)

    def test_first_division_digit_result_type(self):
        """Тест: тип возвращаемого значения"""
        num1 = NaturalFirstDivisionDigit("100")
        num2 = NaturalFirstDivisionDigit("10")
        result = num1.first_division_digit(num2)
        assert isinstance(result, NaturalFirstDivisionDigit)
        assert isinstance(result, Natural)

    def test_first_division_digit_preserves_original_values(self):
        """Тест: исходные числа не изменяются"""
        num1 = NaturalFirstDivisionDigit("100")
        num2 = NaturalFirstDivisionDigit("10")
        original_value1 = num1.value
        original_value2 = num2.value

        result = num1.first_division_digit(num2)

        assert num1.value == original_value1
        assert num2.value == original_value2
        assert result.value == "10"

    def test_first_division_digit_complex_case(self):
        """Тест: сложный случай"""
        num1 = NaturalFirstDivisionDigit("12345")
        num2 = NaturalFirstDivisionDigit("123")
        result = num1.first_division_digit(num2)
        assert result.value == "100"  # 12345/123≈100.36, первая цифра 1, k=2, 1*10^2=100