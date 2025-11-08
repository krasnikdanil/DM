import unittest
from src.polynomial import Polynomial
from src.integer import Integer
from src.rational import Rational

class TestPolynomial(unittest.TestCase):

    def test_creation_and_str(self):
        # Нулевой многочлен
        p = Polynomial()
        self.assertEqual(str(p), "0")
        self.assertTrue(p.is_zero())

        # Многочлен из целых чисел
        p = Polynomial([Integer("1"), Integer("2"), Integer("3")])
        self.assertEqual(str(p), "x^2 + 2x + 3")

        # Многочлен с отрицательными коэффициентами
        p = Polynomial([Integer("1"), Integer("-2"), Integer("3")])
        self.assertEqual(str(p), "x^2 - 2x + 3")

        # Многочлен с ведущим нулем
        p = Polynomial([Integer("0"), Integer("1"), Integer("2")])
        self.assertEqual(str(p), "x + 2")

        # Константа
        p = Polynomial([Integer("5")])
        self.assertEqual(str(p), "5")
        
        # Константа 0
        p = Polynomial([Integer("0")])
        self.assertEqual(str(p), "0")

        # Коэффициент 1 при x
        p = Polynomial([Integer("1"), Integer("0")])
        self.assertEqual(str(p), "x")
        
        # Коэффициент -1
        p = Polynomial([Integer("-1"), Integer("0")])
        self.assertEqual(str(p), "-x")

    def test_equality(self):
        p1 = Polynomial([Integer("1"), Integer("2")])
        p2 = Polynomial([Integer("1"), Integer("2")])
        p3 = Polynomial([Integer("0"), Integer("1"), Integer("2")])
        p4 = Polynomial([Integer("1"), Integer("3")])

        self.assertEqual(p1, p2)
        self.assertEqual(p1, p3) # Ведущие нули должны игнорироваться
        self.assertNotEqual(p1, p4)

    def test_from_rational(self):
        # Создание из Rational
        p = Polynomial([Rational.from_int(Integer("1")), Rational("1", "2")])
        self.assertEqual(str(p), "x + 1/2")

        # Создание из смеси типов
        p = Polynomial([Integer("2"), Rational("1", "3"), "4"])
        self.assertEqual(str(p), "2x^2 + 1/3x + 4")

    def test_is_zero(self):
        p = Polynomial()
        self.assertTrue(p.is_zero())

        p = Polynomial([Integer("0"), Integer("0")])
        self.assertTrue(p.is_zero())

        p = Polynomial([Integer("0"), Integer("1")])
        self.assertFalse(p.is_zero())

if __name__ == '__main__':
    unittest.main()
