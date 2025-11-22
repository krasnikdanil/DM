""" Выполнял Бабуев Бато 4381 """
from typing import List
import re
from rational.rational import Rational
from integer.integer import Integer
from natural.natural import Natural


class Polynomial:
    """
    Класс для работы с многочленами с рациональными коэффициентами.
    Многочлен представлен в виде списка рациональных коэффициентов,
    где индекс элемента соответствует степени переменной.
    Например, [1/2, 0, 3/4] представляет 1/2 + 0*x + 3/4*x^2
    """
    
    def __init__(self, coefficients: List[Rational] = None):
        """
        Инициализация многочлена
        
        :param coefficients: список рациональных коэффициентов
        """
        if coefficients is None:
            self.coefficients = [Rational("0", "1")]
        else:
            # Создаём копию, чтобы не изменять исходный список
            coefficients = coefficients[:]
            # Убираем ведущие нули
            while len(coefficients) > 1 and coefficients[-1].num.is_zero():
                coefficients.pop()
            self.coefficients = coefficients if coefficients else [Rational("0", "1")]
    
    def is_zero(self) -> bool:
        """
        Проверяет, является ли многочлен нулевым
        """
        return len(self.coefficients) == 1 and self.coefficients[0].num.is_zero()
    
    @classmethod
    def from_string(cls, poly_str: str):
        """
        Создание многочлена из строкового представления
        
        :param poly_str: строка вида "2*x^2 + 3*x + 1"
        :return: экземпляр Polynomial
        """
        
        # Удаляем пробелы
        poly_str = poly_str.replace(" ", "")
        
        # Вспомогательная функция для парсинга рациональных чисел
        def _parse_rational(s: str) -> Rational:
            s = s.strip()
            if s.startswith('+'):
                s = s[1:]  # Убираем ведущий плюс
            if '/' in s:
                parts = s.split('/')
                if len(parts) != 2:
                    raise ValueError(f"Некорректная дробь: '{s}'")
                num_part, den_part = parts[0].strip(), parts[1].strip()
                if not den_part or den_part == "0":
                    raise ValueError(f"Нулевой или пустой знаменатель в '{s}'")
                return Rational(num_part, den_part)
            else:
                return Rational(s, "1")
        
        # Разбиваем по знакам + и -
        terms = []
        current_term = ""
        for i, char in enumerate(poly_str):
            if char in ['+', '-'] and i != 0:
                if current_term:
                    terms.append(current_term)
                current_term = char if char == '-' else ''
            else:
                current_term += char
        if current_term:
            terms.append(current_term)
        
        # Создаём словарь для коэффициентов по степеням
        coeffs = {}
        
        for term in terms:
            # Обработка каждого члена
            # Нормализуем: 2x^3 -> 2*x^3, 2x -> 2*x
            # Добавляем * между числом и x (если его нет)
            term = re.sub(r'(\d)x', r'\1*x', term)
            # Добавляем * между дробью и x
            term = re.sub(r'(\d)/(\d+)x', r'\1/\2*x', term)
            
            if '*x^' in term:
                coeff_str, power_str = term.split('*x^')
                power = int(power_str)
                if coeff_str in ['+', '']:
                    coeff_str = '1'
                elif coeff_str == '-':
                    coeff_str = '-1'
                coeff = _parse_rational(coeff_str)
                coeffs[power] = coeff
            elif term.startswith('x^') or term.startswith('-x^'):
                # Обработка x^n без коэффициента (например, x^2 или -x^2)
                if term.startswith('-'):
                    coeff_str = '-1'
                    power_str = term[3:]  # убираем '-x^'
                else:
                    coeff_str = '1'
                    power_str = term[2:]  # убираем 'x^'
                power = int(power_str)
                coeff = _parse_rational(coeff_str)
                coeffs[power] = coeff
            elif term.endswith('*x'):
                coeff_str = term[:-2]
                if coeff_str in ['+', '']:
                    coeff_str = '1'
                elif coeff_str == '-':
                    coeff_str = '-1'
                coeff = _parse_rational(coeff_str)
                coeffs[1] = coeff
            elif term == 'x':
                coeffs[1] = _parse_rational("1")
            elif term == '-x':
                coeffs[1] = _parse_rational("-1")
            else:
                # Свободный член
                if term and term not in ['+', '-', '']:  # Проверяем, что строка не пустая
                    coeff = _parse_rational(term)
                    coeffs[0] = coeff
        
        # Находим максимальную степень
        max_degree = max(coeffs.keys()) if coeffs else 0
        
        # Создаём список коэфициентов
        result_coeffs = []
        for i in range(max_degree + 1):
            if i in coeffs:
                result_coeffs.append(coeffs[i])
            else:
                result_coeffs.append(Rational("0", "1"))
        
        return cls(result_coeffs)
    
    def __str__(self) -> str:
        """
        Строковое представление многочлена (от старшей степени к младшей)
        """
        if not self.coefficients:
            return "0"
        
        terms = []
        # Идём от старшей степени (конец списка) к младшей (начало списка)
        for i in range(len(self.coefficients) - 1, -1, -1):
            coeff = self.coefficients[i]
            if not coeff.num.is_zero():
                coeff_str = str(coeff)
                if i == 0:
                    # Свободный член
                    is_negative = coeff_str.startswith('-')
                    abs_coeff = coeff_str[1:] if is_negative else coeff_str
                    terms.append((abs_coeff, is_negative))
                elif i == 1:
                    # x в первой степени
                    if coeff_str == "1":
                        terms.append(("x", False))
                    elif coeff_str == "-1":
                        terms.append(("x", True))
                    else:
                        is_negative = coeff_str.startswith('-')
                        abs_coeff = coeff_str[1:] if is_negative else coeff_str
                        terms.append((f"{abs_coeff}*x", is_negative))
                else:
                    # x в степени > 1
                    if coeff_str == "1":
                        terms.append((f"x^{i}", False))
                    elif coeff_str == "-1":
                        terms.append((f"x^{i}", True))
                    else:
                        is_negative = coeff_str.startswith('-')
                        abs_coeff = coeff_str[1:] if is_negative else coeff_str
                        terms.append((f"{abs_coeff}*x^{i}", is_negative))
        
        if not terms:
            return "0"
        
        # Формируем строку
        result = ""
        for idx, (term, is_negative) in enumerate(terms):
            if idx == 0:
                # Первый член
                if is_negative:
                    result = f"-{term}"
                else:
                    result = term
            else:
                # Последующие члены
                if is_negative:
                    result += f" - {term}"
                else:
                    result += f" + {term}"
        
        return result
    
    def __repr__(self) -> str:
        return f"Polynomial({self.coefficients})"
    
    # P-1: Сложение многочленов
    def add_pp_p(self, other: Polynomial) -> Polynomial:
        """
        Сложение многочленов
        """
        result_coeffs = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else Rational("0", "1")
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else Rational("0", "1")
            result_coeffs.append(coeff1 + coeff2)
        
        return Polynomial(result_coeffs)
    
    def add_pq_p(self, other: Rational) -> Polynomial:
        """
        Сложение многочлена с рациональным числом (свободным членом)
        """
        result_coeffs = self.coefficients[:]
        result_coeffs[0] = result_coeffs[0] + other
        return Polynomial(result_coeffs)
    
    # P-2: Вычитание многочленов
    def sub_pp_p(self, other: Polynomial) -> Polynomial:
        """
        Вычитание многочленов
        """
        result_coeffs = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else Rational("0", "1")
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else Rational("0", "1")
            result_coeffs.append(coeff1 - coeff2)
        
        return Polynomial(result_coeffs)
    
    def sub_pq_p(self, other: Rational) -> Polynomial:
        """
        Вычитание рационального числа (свободного члена) из многочлена
        """
        result_coeffs = self.coefficients[:]
        result_coeffs[0] = result_coeffs[0] - other
        return Polynomial(result_coeffs)
    
    # P-3: Умножение многочлена на рациональное число
    def mul_pq_p(self, other: Rational) -> Polynomial:
        """
        Умножение многочлена на рациональное число
        """
        result_coeffs = []
        for coeff in self.coefficients:
            result_coeffs.append(coeff * other)
        
        return Polynomial(result_coeffs)
    
    
    # P-4: Умножение многочлена на x^k
    def mul_pxk_p(self, k: Natural) -> Polynomial:
        """
        Умножение многочлена на x^k, где k - натуральное или 0
        """
        # Преобразуем Natural в int для использования
        k_int = int(str(k))
        
        if k_int < 0:
            raise ValueError("k должно быть натуральным числом или 0")
        
        if k_int == 0:
            return Polynomial(self.coefficients[:])
        
        result_coeffs = [Rational("0", "1")] * k_int + self.coefficients
        return Polynomial(result_coeffs)
    
    # P-5: Старший коэффициент многочлена
    def led_p_q(self) -> Rational:
        """
        Старший коэффициент многочлена
        """
        if self.is_zero():
            return Rational("0", "1")
        return self.coefficients[-1]
    
    # P-6: Степень многочлена
    def deg_p_n(self) -> Natural:
        """
        Степень многочлена
        """
        if self.is_zero():
            return Natural("0")
        return Natural(str(len(self.coefficients) - 1))
    
    # P-7: Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def fac_p_q(self) -> Rational:
        """
        Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
        """
        if self.is_zero():
            return Rational("0", "1")
        
        numerators = []
        denominators = []
        
        for coeff in self.coefficients:
            if not coeff.num.is_zero():
                numerators.append(abs(coeff.num))
                denominators.append(coeff.den)
        
        if not numerators:
            return Rational("0", "1")
        
        # Находим НОД числителей
        gcd_numerators = numerators[0]
        for i in range(1, len(numerators)):
            gcd_numerators = gcd_numerators.gcd(numerators[i])
        
        # Находим НОК знаменателей
        lcm_denominators = denominators[0]
        for i in range(1, len(denominators)):
            lcm_denominators = lcm_denominators.lcm(denominators[i])
        
        # Возвращаем НОД(числителей)/НОК(знаменателей)
        return Rational(str(Integer.from_natural(gcd_numerators)), str(lcm_denominators))
    
    # P-8: Умножение многочленов
    def mul_pp_p(self, other: Polynomial) -> Polynomial:
        """
        Умножение многочленов
        """
        if not self.coefficients or not other.coefficients:
            return Polynomial([Rational("0", "1")])
        
        # Результат будет иметь степень len1 + len2 - 2
        result_len = len(self.coefficients) + len(other.coefficients) - 1
        result_coeffs = [Rational("0", "1")] * result_len
        
        for i, coeff1 in enumerate(self.coefficients):
            for j, coeff2 in enumerate(other.coefficients):
                result_coeffs[i + j] += coeff1 * coeff2
        
        return Polynomial(result_coeffs)
    
    # P-9: Частное от деления многочлена на многочлен при делении с остатком
    def div_pp_p(self, other: Polynomial) -> Polynomial:
        """
        Частное от деления многочлена на многочлен при делении с остатком
        """
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")

        dividend = Polynomial(self.coefficients[:])
        divisor = other

        if dividend.deg_p_n() < divisor.deg_p_n():
            return Polynomial()

        # Правильное вычисление разности степеней
        deg_dividend = dividend.deg_p_n()
        deg_divisor = divisor.deg_p_n()
        quotient_len = int(str(deg_dividend - deg_divisor)) + 1
        quotient_coeffs = [Rational("0", "1")] * quotient_len
        
        lead_divisor = divisor.led_p_q()

        while not dividend.is_zero() and dividend.deg_p_n() >= divisor.deg_p_n():
            deg_diff = int(str(dividend.deg_p_n() - divisor.deg_p_n()))
            lead_dividend = dividend.led_p_q()
            
            term_coeff = lead_dividend / lead_divisor
            quotient_coeffs[deg_diff] = term_coeff
            
            term_poly = Polynomial([term_coeff]).mul_pxk_p(Natural(str(deg_diff)))
            
            subtrahend = divisor.mul_pp_p(term_poly)
            dividend -= subtrahend
        
        return Polynomial(quotient_coeffs)
    
    # P-10: Остаток от деления многочлена на многочлен при делении с остатком
    def mod_pp_p(self, other: Polynomial) -> Polynomial:
        """
        Остаток от деления многочлена на многочлен при делении с остатком
        """
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
        quotient = self.div_pp_p(other)
        product = quotient.mul_pp_p(other)
        remainder = self.sub_pp_p(product)
        
        return remainder
    
    # P-11: НОД многочленов
    def gcf_pp_p(self, other: Polynomial) -> Polynomial:
        """
        НОД многочленов
        """
        # Используем алгоритм Евклида для многочленов
        a = Polynomial(self.coefficients[:])
        b = Polynomial(other.coefficients[:])
        
        # Убираем нулевые многочлены
        while not b.is_zero():
            remainder = a.mod_pp_p(b)
            a = b
            b = remainder
        
        # Нормализуем НОД, чтобы получить монический многочлен (старший коэффициент = 1)
        lead_coeff = a.led_p_q()
        if not lead_coeff.num.is_zero():
            # Создаём обратное рациональное число правильно
            inverse = Rational(str(lead_coeff.den), str(abs(lead_coeff.num)))
            if lead_coeff.num.is_negative():
                inverse.num = -inverse.num
            return a.mul_pq_p(inverse)
        else:
            return Polynomial()
    
    # P-12: Производная многочлена
    def der_p_p(self) -> Polynomial:
        """
        Производная многочлена
        """
        if len(self.coefficients) <= 1:
            # Производная константы равна 0
            return Polynomial([Rational("0", "1")])
        
        result_coeffs = []
        for i in range(1, len(self.coefficients)):
            # Производная a_i * x^i равна i * a_i * x^(i-1)
            coeff = self.coefficients[i]
            # Умножаем коэффициент на степень
            new_coeff = coeff * Rational(str(i), "1")
            result_coeffs.append(new_coeff)

        return Polynomial(result_coeffs)
    
    # P-13: Преобразование многочлена — кратные корни в простые
    def nmr_p_p(self) -> Polynomial:
        """
        Преобразование многочлена — кратные корни в простые
        """
        # Если многочлен константа, возвращаем его же
        if len(self.coefficients) <= 1:
            return Polynomial(self.coefficients[:])
        
        # Находим НОД многочлена и его производной
        derivative = self.der_p_p()
        
        # Если производная - нулевой многочлен (многочлен степени 0 или 1),
        # то у него нет кратных корней, возвращаем исходный многочлен
        if derivative.is_zero():
            return Polynomial(self.coefficients[:])
        
        gcd_poly = self.gcf_pp_p(derivative)

        if gcd_poly.is_zero():
            return Polynomial(self.coefficients[:])
        
        result = self.div_pp_p(gcd_poly)
        
        return result
    
    
    def __add__(self, other):
        if isinstance(other, Polynomial):
            return self.add_pp_p(other)
        elif isinstance(other, Rational):
            return self.add_pq_p(other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            return self.sub_pp_p(other)
        elif isinstance(other, Rational):
            return self.sub_pq_p(other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            return self.mul_pp_p(other)
        elif isinstance(other, Rational):
            return self.mul_pq_p(other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Polynomial):
            return self.div_pp_p(other)
        return NotImplemented
    
    def __mod__(self, other):
        if isinstance(other, Polynomial):
            return self.mod_pp_p(other)
        return NotImplemented
    
    def __eq__(self, other) -> bool:
        """Проверка равенства многочленов"""
        if not isinstance(other, Polynomial):
            return NotImplemented
        if len(self.coefficients) != len(other.coefficients):
            return False
        for c1, c2 in zip(self.coefficients, other.coefficients):
            # Сравниваем рациональные коэффициенты через сокращение
            if str(c1.red_q_q()) != str(c2.red_q_q()):
                return False
        return True
    
    def __ne__(self, other) -> bool:
        """Проверка неравенства многочленов"""
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
