import unittest
import sys
import os

# Добавляем путь к src в sys.path для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.polynomial.polynomial import Polynomial
from src.rational.rational import Rational


class TestPolynomial(unittest.TestCase):
    
    def test_init(self):
        """Тест инициализации многочлена"""
        # Пустая инициализация
        p = Polynomial()
        self.assertEqual(str(p), "0")
        
        # Инициализация с коэффициентами
        p = Polynomial([Rational("1", "1"), Rational("2", "1"), Rational("3", "1")])
        self.assertEqual(str(p), "1 + 2*x + 3*x^2")
        
        # Инициализация с ведущими нулями
        p = Polynomial([Rational("1", "1"), Rational("2", "1"), Rational("0", "1")])
        self.assertEqual(str(p), "1 + 2*x")
    
    def test_from_string(self):
        """Тест создания многочлена из строки"""
        p = Polynomial.from_string("2*x^2 + 3*x + 1")
        self.assertEqual(str(p), "1 + 3*x + 2*x^2")
        
        p = Polynomial.from_string("x^3 - 2*x + 5")
        self.assertEqual(str(p), "5 - 2*x + x^3")
        
        p = Polynomial.from_string("-x^2 + 3*x - 1")
        self.assertEqual(str(p), "-1 + 3*x - x^2")
    
    def test_add_pp_p(self):
        """Тест сложения многочленов"""
        p1 = Polynomial([Rational("1", "1"), Rational("2", "1")])  # 1 + 2*x
        p2 = Polynomial([Rational("3", "1"), Rational("4", "1")])  # 3 + 4*x
        result = p1.add_pp_p(p2)
        self.assertEqual(str(result), "4 + 6*x")
    
    def test_sub_pp_p(self):
        """Тест вычитания многочленов"""
        p1 = Polynomial([Rational("5", "1"), Rational("3", "1")])  # 5 + 3*x
        p2 = Polynomial([Rational("2", "1"), Rational("1", "1")])  # 2 + x
        result = p1.sub_pp_p(p2)
        self.assertEqual(str(result), "3 + 2*x")
    
    def test_mul_pq_p(self):
        """Тест умножения многочлена на рациональное число"""
        p = Polynomial([Rational("1", "1"), Rational("2", "1"), Rational("3", "1")])  # 1 + 2*x + 3*x^2
        result = p.mul_pq_p(Rational("2", "1"))
        self.assertEqual(str(result), "2 + 4*x + 6*x^2")
    
    def test_mul_pxk_p(self):
        """Тест умножения многочлена на x^k"""
        p = Polynomial([Rational("1", "1"), Rational("2", "1")])  # 1 + 2*x
        result = p.mul_pxk_p(2)  # (1 + 2*x) * x^2 = x^2 + 2*x^3
        self.assertEqual(str(result), "x^2 + 2*x^3")
    
    def test_led_p_q(self):
        """Тест получения старшего коэффициента"""
        p = Polynomial([Rational("1", "1"), Rational("2", "1"), Rational("3", "1")])  # 1 + 2*x + 3*x^2
        self.assertEqual(str(p.led_p_q()), "3/1")
        
        p = Polynomial([Rational("5", "1")])  # 5
        self.assertEqual(str(p.led_p_q()), "5/1")
        
        p = Polynomial([Rational("0", "1")])  # 0
        self.assertEqual(str(p.led_p_q()), "0/1")
    
    def test_deg_p_n(self):
        """Тест получения степени многочлена"""
        p = Polynomial([Rational("1", "1"), Rational("2", "1"), Rational("3", "1")])  # 1 + 2*x + 3*x^2
        self.assertEqual(p.deg_p_n(), 2)
        
        p = Polynomial([Rational("5", "1")])  # 5
        self.assertEqual(p.deg_p_n(), 0)
        
        p = Polynomial([Rational("0", "1")])  # 0
        self.assertEqual(p.deg_p_n(), 0)
    
    def test_mul_pp_p(self):
        """Тест умножения многочленов"""
        p1 = Polynomial([Rational("1", "1"), Rational("1", "1")])  # 1 + x
        p2 = Polynomial([Rational("1", "1"), Rational("1", "1")])  # 1 + x
        result = p1.mul_pp_p(p2)  # (1+x) * (1+x) = 1 + 2*x + x^2
        self.assertEqual(str(result), "1 + 2*x + x^2")
    
    def test_div_pp_p(self):
        """Тест деления многочленов"""
        p1 = Polynomial([Rational("1", "1"), Rational("3", "1"), Rational("2", "1")])  # 1 + 3*x + 2*x^2 = (1+x)(1+2x)
        p2 = Polynomial([Rational("1", "1"), Rational("1", "1")])  # 1 + x
        result = p1.div_pp_p(p2)
        self.assertEqual(str(result), "1 + 2*x")
    
    def test_mod_pp_p(self):
        """Тест остатка от деления многочленов"""
        p1 = Polynomial([Rational("1", "1"), Rational("3", "1"), Rational("2", "1")])  # 1 + 3*x + 2*x^2
        p2 = Polynomial([Rational("1", "1"), Rational("1", "1")])  # 1 + x
        remainder = p1.mod_pp_p(p2)
        self.assertEqual(str(remainder), "0")
    
    def test_gcf_pp_p(self):
        """Тест НОД многочленов"""
        p1 = Polynomial([Rational("2", "1"), Rational("4", "1"), Rational("2", "1")])  # 2 + 4*x + 2*x^2 = 2(1+x)^2
        p2 = Polynomial([Rational("1", "1"), Rational("1", "1")])  # 1 + x
        result = p1.gcf_pp_p(p2)
        # НОД(2(1+x)^2, 1+x) = 1+x, но нормализованный (старший коэффициент = 1)
        self.assertEqual(str(result), "1 + x")
    
    def test_der_p_p(self):
        """Тест производной многочлена"""
        p = Polynomial([Rational("1", "1"), Rational("2", "1"), Rational("3", "1")])  # 1 + 2*x + 3*x^2
        result = p.der_p_p()  # 2 + 6*x
        self.assertEqual(str(result), "2 + 6*x")
    
    def test_nmr_p_p(self):
        """Тест преобразования кратных корней в простые"""
        # Многочлен с кратными корнями: (x+1)^2 = x^2 + 2*x + 1
        p = Polynomial([Rational("1", "1"), Rational("2", "1"), Rational("1", "1")])
        result = p.nmr_p_p()  # Результат должен быть x+1 (корни превращаются в простые)
        # Результат может быть нормализован, поэтому проверим степень
        self.assertEqual(result.deg_p_n(), 1)


if __name__ == '__main__':
    unittest.main()