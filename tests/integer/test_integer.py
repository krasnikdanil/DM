import unittest
from src.integer.integer import Integer
from src.natural.natural import Natural

class TestIntegerCreation(unittest.TestCase):
    def test_best_cases(self):
        self.assertEqual(str(Integer("123")), "123")
        self.assertEqual(str(Integer("-456")), "-456")
        self.assertEqual(str(Integer("+789")), "789")
        self.assertEqual(str(Integer("0")), "0")
        self.assertEqual(str(Integer("-0")), "0")

    def test_worst_cases(self):
        with self.assertRaises(TypeError):
            Integer(123)
        with self.assertRaises(ValueError):
            Integer("abc")
        with self.assertRaises(ValueError):
            Integer("-abc")
        with self.assertRaises(ValueError):
            Integer("12-3")

    def test_negation(self):
        self.assertEqual(str(-Integer("123")), "-123")
        self.assertEqual(str(-Integer("-456")), "456")
        self.assertEqual(str(-Integer("0")), "0")

class TestIntegerAddition(unittest.TestCase):
    def test_best_cases(self):
        self.assertEqual(str(Integer("5") + Integer("3")), "8")
        self.assertEqual(str(Integer("-5") + Integer("-3")), "-8")
        self.assertEqual(str(Integer("8") + Integer("-3")), "5")
        self.assertEqual(str(Integer("-8") + Integer("3")), "-5")
        self.assertEqual(str(Integer("3") + Integer("-8")), "-5")
        self.assertEqual(str(Integer("-3") + Integer("8")), "5")
        self.assertEqual(str(Integer("5") + Integer("-5")), "0")

    def test_with_zero(self):
        self.assertEqual(str(Integer("123") + Integer("0")), "123")
        self.assertEqual(str(Integer("-123") + Integer("0")), "-123")
        self.assertEqual(str(Integer("0") + Integer("123")), "123")
        self.assertEqual(str(Integer("0") + Integer("-123")), "-123")
        self.assertEqual(str(Integer("0") + Integer("0")), "0")

class TestIntegerSubtraction(unittest.TestCase):
    def test_best_cases(self):
        self.assertEqual(str(Integer("5") - Integer("3")), "2")
        self.assertEqual(str(Integer("3") - Integer("5")), "-2")
        self.assertEqual(str(Integer("-5") - Integer("-3")), "-2")
        self.assertEqual(str(Integer("-3") - Integer("-5")), "2")
        self.assertEqual(str(Integer("5") - Integer("-3")), "8")
        self.assertEqual(str(Integer("-5") - Integer("3")), "-8")

    def test_with_zero(self):
        self.assertEqual(str(Integer("123") - Integer("0")), "123")
        self.assertEqual(str(Integer("0") - Integer("123")), "-123")
        self.assertEqual(str(Integer("-123") - Integer("0")), "-123")
        self.assertEqual(str(Integer("0") - Integer("-123")), "123")

class TestIntegerMultiplication(unittest.TestCase):
    def test_best_cases(self):
        self.assertEqual(str(Integer("5") * Integer("3")), "15")
        self.assertEqual(str(Integer("-5") * Integer("3")), "-15")
        self.assertEqual(str(Integer("5") * Integer("-3")), "-15")
        self.assertEqual(str(Integer("-5") * Integer("-3")), "15")

    def test_with_zero_and_one(self):
        self.assertEqual(str(Integer("123") * Integer("0")), "0")
        self.assertEqual(str(Integer("-123") * Integer("0")), "0")
        self.assertEqual(str(Integer("123") * Integer("1")), "123")
        self.assertEqual(str(Integer("-123") * Integer("-1")), "123")

class TestIntegerDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(str(Integer("10") // Integer("3")), "3")
        self.assertEqual(str(Integer("-10") // Integer("3")), "-4")
        self.assertEqual(str(Integer("10") // Integer("-3")), "-4")
        self.assertEqual(str(Integer("-10") // Integer("-3")), "3")
        self.assertEqual(str(Integer("10") // Integer("2")), "5")
        self.assertEqual(str(Integer("-10") // Integer("2")), "-5")

    def test_modulus(self):
        self.assertEqual(str(Integer("10") % Integer("3")), "1")
        self.assertEqual(str(Integer("-10") % Integer("3")), "2")
        self.assertEqual(str(Integer("10") % Integer("-3")), "-2")
        self.assertEqual(str(Integer("-10") % Integer("-3")), "-1")
        self.assertEqual(str(Integer("10") % Integer("2")), "0")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Integer("10") // Integer("0")
        with self.assertRaises(ZeroDivisionError):
            Integer("10") % Integer("0")

class TestIntegerHelpers(unittest.TestCase):
    def test_abs(self):
        self.assertEqual(abs(Integer("123")), Natural("123"))
        self.assertEqual(abs(Integer("-123")), Natural("123"))
        self.assertEqual(abs(Integer("0")), Natural("0"))

    def test_poz(self):
        self.assertEqual(Integer("123").poz(), 1)
        self.assertEqual(Integer("-123").poz(), -1)
        self.assertEqual(Integer("0").poz(), 0)

    def test_from_natural(self):
        n = Natural("456")
        i = Integer.from_natural(n)
        self.assertIsInstance(i, Integer)
        self.assertEqual(str(i), "456")

    def test_to_natural(self):
        i_pos = Integer("789")
        i_zero = Integer("0")
        i_neg = Integer("-123")
        n = i_pos.to_natural()
        self.assertIsInstance(n, Natural)
        self.assertEqual(str(n), "789")
        self.assertEqual(str(i_zero.to_natural()), "0")
        with self.assertRaises(ValueError):
            i_neg.to_natural()

if __name__ == '__main__':
    unittest.main()
