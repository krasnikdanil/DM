import unittest
from src.natural.natural import Natural

class TestNaturalClass(unittest.TestCase):

    def test_init_and_str(self):
        # Хорошие варианты
        self.assertEqual(str(Natural("123")), "123")
        self.assertEqual(str(Natural("0")), "0")
        self.assertEqual(str(Natural()), "0")
        self.assertEqual(str(Natural("98765432109876543210")), "98765432109876543210")

        # Плохие варианты (ожидаем ошибки)
        with self.assertRaises(ValueError, msg="Должна быть ошибка для нечисловых строк"):
            Natural("abc")
        with self.assertRaises(ValueError, msg="Должна быть ошибка для отрицательных чисел"):
            Natural("-123")
        with self.assertRaises(ValueError, msg="Должна быть ошибка для пустой строки"):
            Natural("")

    def test_comparison(self):
        # Хорошие варианты
        self.assertTrue(Natural("123") > Natural("100"))
        self.assertFalse(Natural("100") > Natural("123"))
        self.assertTrue(Natural("100") < Natural("123"))
        self.assertFalse(Natural("123") < Natural("100"))
        self.assertTrue(Natural("123") == Natural("123"))
        self.assertFalse(Natural("123") == Natural("100"))
        self.assertTrue(Natural("123") != Natural("100"))
        self.assertFalse(Natural("123") != Natural("123"))
        self.assertTrue(Natural("123") >= Natural("123"))
        self.assertTrue(Natural("123") >= Natural("100"))
        self.assertTrue(Natural("123") <= Natural("123"))
        self.assertTrue(Natural("100") <= Natural("123"))
        
        # Пограничные случаи
        self.assertTrue(Natural("1000") > Natural("999"))
        self.assertFalse(Natural("999") > Natural("1000"))

    def test_add(self):
        # Хорошие варианты
        self.assertEqual(Natural("123") + Natural("456"), Natural("579"))
        self.assertEqual(Natural("99") + Natural("1"), Natural("100"))
        self.assertEqual(Natural("1") + Natural("999"), Natural("1000"))
        
        # Пограничные случаи
        self.assertEqual(Natural("123") + Natural("0"), Natural("123"))
        self.assertEqual(Natural("0") + Natural("123"), Natural("123"))
        self.assertEqual(Natural("0") + Natural("0"), Natural("0"))

    def test_sub(self):
        # Хорошие варианты
        self.assertEqual(Natural("579") - Natural("456"), Natural("123"))
        self.assertEqual(Natural("100") - Natural("1"), Natural("99"))
        
        # Пограничные случаи
        self.assertEqual(Natural("123") - Natural("0"), Natural("123"))
        self.assertEqual(Natural("123") - Natural("123"), Natural("0"))
        self.assertEqual(Natural("1000") - Natural("999"), Natural("1"))
        
        # Плохие варианты (ожидаем ошибку)
        with self.assertRaises(ValueError, msg="Вычитание меньшего из большего должно вызывать ошибку"):
            Natural("100") - Natural("101")

    def test_mul(self):
        # Хорошие варианты
        self.assertEqual(Natural("12") * Natural("10"), Natural("120"))
        self.assertEqual(Natural("123") * Natural("45"), Natural("5535"))
        
        # Пограничные случаи
        self.assertEqual(Natural("99") * Natural("0"), Natural("0"))
        self.assertEqual(Natural("0") * Natural("99"), Natural("0"))
        self.assertEqual(Natural("12345") * Natural("1"), Natural("12345"))

    def test_floordiv(self):
        # Хорошие варианты
        self.assertEqual(Natural("120") // Natural("10"), Natural("12"))
        self.assertEqual(Natural("5535") // Natural("45"), Natural("123"))
        self.assertEqual(Natural("128") // Natural("5"), Natural("25"))
        
        # Пограничные случаи
        self.assertEqual(Natural("99") // Natural("100"), Natural("0"))
        self.assertEqual(Natural("100") // Natural("100"), Natural("1"))
        self.assertEqual(Natural("0") // Natural("123"), Natural("0"))
        
        # Плохие варианты (ожидаем ошибку)
        with self.assertRaises(ZeroDivisionError, msg="Деление на ноль должно вызывать ошибку"):
            Natural("100") // Natural("0")

    def test_mod(self):
        # Хорошие варианты
        self.assertEqual(Natural("128") % Natural("5"), Natural("3"))
        self.assertEqual(Natural("120") % Natural("10"), Natural("0"))
        
        # Пограничные случаи
        self.assertEqual(Natural("5") % Natural("128"), Natural("5"))
        self.assertEqual(Natural("100") % Natural("100"), Natural("0"))
        self.assertEqual(Natural("0") % Natural("123"), Natural("0"))
        
        # Плохие варианты (ожидаем ошибку)
        with self.assertRaises(ZeroDivisionError, msg="Взятие остатка от деления на ноль должно вызывать ошибку"):
            Natural("100") % Natural("0")

    def test_mul_10k(self):
        # Хорошие варианты
        self.assertEqual(Natural("123").mul_10k(2), Natural("12300"))
        self.assertEqual(Natural("7").mul_10k(3), Natural("7000"))
        
        # Пограничные случаи
        self.assertEqual(Natural("45").mul_10k(0), Natural("45"))
        self.assertEqual(Natural("0").mul_10k(5), Natural("0"))
        
        # Плохие варианты (ожидаем ошибку)
        with self.assertRaises(ValueError, msg="Степень k не может быть отрицательной"):
            Natural("123").mul_10k(-1)

    def test_div_first_digit(self):
        # Хорошие варианты
        self.assertEqual(Natural("582").div_first_digit(Natural("7")), (8, 1))
        self.assertEqual(Natural("12345").div_first_digit(Natural("2")), (6, 3))
        
        # Пограничные случаи
        self.assertEqual(Natural("100").div_first_digit(Natural("101")), (0, 0))
        self.assertEqual(Natural("999").div_first_digit(Natural("100")), (9, 0))
        self.assertEqual(Natural("899").div_first_digit(Natural("100")), (8, 0))

    def test_gcd(self):
        # Хорошие варианты
        self.assertEqual(Natural("48").gcd(Natural("18")), Natural("6"))
        self.assertEqual(Natural("101").gcd(Natural("10")), Natural("1"))
        
        # Пограничные случаи
        self.assertEqual(Natural("7").gcd(Natural("0")), Natural("7"))
        self.assertEqual(Natural("0").gcd(Natural("7")), Natural("7"))
        self.assertEqual(Natural("123").gcd(Natural("123")), Natural("123"))

    def test_lcm(self):
        # Хорошие варианты
        self.assertEqual(Natural("48").lcm(Natural("18")), Natural("144"))
        self.assertEqual(Natural("12").lcm(Natural("13")), Natural("156"))
        
        # Пограничные случаи
        self.assertEqual(Natural("7").lcm(Natural("0")), Natural("0"))
        self.assertEqual(Natural("0").lcm(Natural("7")), Natural("0"))
        self.assertEqual(Natural("123").lcm(Natural("1")), Natural("123"))

if __name__ == '__main__':
    unittest.main()
