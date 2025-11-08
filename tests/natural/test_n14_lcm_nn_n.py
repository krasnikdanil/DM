import pytest
from src.natural.n14_lcm_nn_n import NaturalLCM
from src.natural.natural import Natural


class TestNaturalLCM:
    def test_lcm_simple_case(self):
        """Тест: простой случай"""
        num1 = NaturalLCM("4")
        num2 = NaturalLCM("6")
        result = num1.lcm(num2)
        assert result.value == "12"

    def test_lcm_coprime_numbers(self):
        """Тест: взаимно простые числа"""
        num1 = NaturalLCM("5")
        num2 = NaturalLCM("7")
        result = num1.lcm(num2)
        assert result.value == "35"

    def test_lcm_equal_numbers(self):
        """Тест: равные числа"""
        num1 = NaturalLCM("8")
        num2 = NaturalLCM("8")
        result = num1.lcm(num2)
        assert result.value == "8"

    def test_lcm_one_is_multiple_of_other(self):
        """Тест: одно число кратно другому"""
        num1 = NaturalLCM("12")
        num2 = NaturalLCM("4")
        result = num1.lcm(num2)
        assert result.value == "12"

        num1 = NaturalLCM("3")
        num2 = NaturalLCM("15")
        result = num1.lcm(num2)
        assert result.value == "15"

    def test_lcm_prime_numbers(self):
        """Тест: простые числа"""
        num1 = NaturalLCM("11")
        num2 = NaturalLCM("13")
        result = num1.lcm(num2)
        assert result.value == "143"

    def test_lcm_large_numbers(self):
        """Тест: большие числа"""
        num1 = NaturalLCM("100")
        num2 = NaturalLCM("125")
        result = num1.lcm(num2)
        assert result.value == "500"

    def test_lcm_with_one(self):
        """Тест: числа с единицей"""
        num1 = NaturalLCM("1")
        num2 = NaturalLCM("15")
        result = num1.lcm(num2)
        assert result.value == "15"

        num1 = NaturalLCM("23")
        num2 = NaturalLCM("1")
        result = num1.lcm(num2)
        assert result.value == "23"

    def test_lcm_commutative(self):
        """Тест: коммутативность НОК"""
        num1 = NaturalLCM("12")
        num2 = NaturalLCM("18")
        result1 = num1.lcm(num2)
        result2 = num2.lcm(num1)
        assert result1.value == result2.value
        assert result1.value == "36"

    def test_lcm_three_numbers_chain(self):
        """Тест: цепочка из трех чисел"""
        num1 = NaturalLCM("4")
        num2 = NaturalLCM("6")
        num3 = NaturalLCM("8")
        result1 = num1.lcm(num2)  # НОК(4,6)=12
        result2 = result1.lcm(num3)  # НОК(12,8)=24
        assert result2.value == "24"

    def test_lcm_zero_first_number(self):
        """Тест: первое число ноль"""
        num1 = NaturalLCM("0")
        num2 = NaturalLCM("5")
        with pytest.raises(ValueError):
            num1.lcm(num2)

    def test_lcm_zero_second_number(self):
        """Тест: второе число ноль"""
        num1 = NaturalLCM("7")
        num2 = NaturalLCM("0")
        with pytest.raises(ValueError):
            num1.lcm(num2)

    def test_lcm_both_zero(self):
        """Тест: оба числа ноль"""
        num1 = NaturalLCM("0")
        num2 = NaturalLCM("0")
        with pytest.raises(ValueError):
            num1.lcm(num2)

    def test_lcm_small_numbers(self):
        """Тест: маленькие числа"""
        num1 = NaturalLCM("2")
        num2 = NaturalLCM("3")
        result = num1.lcm(num2)
        assert result.value == "6"

    def test_lcm_result_type(self):
        """Тест: тип возвращаемого значения"""
        num1 = NaturalLCM("10")
        num2 = NaturalLCM("15")
        result = num1.lcm(num2)
        assert isinstance(result, NaturalLCM)
        assert isinstance(result, Natural)

    def test_lcm_preserves_original_values(self):
        """Тест: исходные числа не изменяются"""
        num1 = NaturalLCM("10")
        num2 = NaturalLCM("15")
        original_value1 = num1.value
        original_value2 = num2.value

        result = num1.lcm(num2)

        assert num1.value == original_value1
        assert num2.value == original_value2
        assert result.value == "30"

    def test_lcm_property_with_gcd(self):
        """Тест: свойство НОК × НОД = a × b"""
        import math
        num1 = NaturalLCM("12")
        num2 = NaturalLCM("18")
        lcm_result = num1.lcm(num2)
        gcd_val = math.gcd(12, 18)
        assert int(lcm_result.value) * gcd_val == 12 * 18

    def test_lcm_edge_case_large_primes(self):
        """Тест: граничный случай - большие простые числа"""
        num1 = NaturalLCM("997")  # простое число
        num2 = NaturalLCM("991")  # простое число
        result = num1.lcm(num2)
        assert result.value == str(997 * 991)