from typing import List
from src.rational.rational import Rational
from src.integer.integer import Integer
from src.natural.natural import Natural


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
            # Убираем ведущие нули
            while len(coefficients) > 1 and str(coefficients[-1].num) == "0":
                coefficients.pop()
            self.coefficients = coefficients if coefficients else [Rational("0", "1")]
    
    def is_zero(self) -> bool:
        """
        Проверяет, является ли многочлен нулевым
        """
        return len(self.coefficients) == 1 and str(self.coefficients[0].num) == "0"
    
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
                current_term = char
            else:
                current_term += char
        if current_term:
            terms.append(current_term)
        
        # Создаём словарь для коэффициентов по степеням
        coeffs = {}
        
        for term in terms:
            # Обработка каждого члена
            if '*x^' in term:
                coeff_str, power_str = term.split('*x^')
                power = int(power_str)
                if coeff_str in ['+', '']:
                    coeff_str = '1'
                elif coeff_str == '-':
                    coeff_str = '-1'
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
        Строковое представление многочлена
        """
        if not self.coefficients:
            return "0"
        
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if str(coeff.num) != "0":
                coeff_str = str(coeff)
                if i == 0:
                    terms.append(coeff_str)
                elif i == 1:
                    if coeff_str == "1":
                        terms.append("x")
                    elif coeff_str == "-1":
                        terms.append("-x")
                    else:
                        terms.append(f"{coeff_str}*x")
                else:
                    if coeff_str == "1":
                        terms.append(f"x^{i}")
                    elif coeff_str == "-1":
                        terms.append(f"-x^{i}")
                    else:
                        terms.append(f"{coeff_str}*x^{i}")
        
        if not terms:
            return "0"
        
        result = terms[0]
        for term in terms[1:]:
            if term.startswith('-'):
                result += f" - {term[1:]}"
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
            result_coeffs.append(coeff1.add_qq_q(coeff2))
        
        return Polynomial(result_coeffs)
    
    def add_qq_q(self, other: Rational) -> Polynomial:
        """
        Сложение многочлена с рациональным числом (свободным членом)
        """
        result_coeffs = self.coefficients[:]
        result_coeffs[0] = result_coeffs[0].add_qq_q(other)
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
            result_coeffs.append(coeff1.sub_qq_q(coeff2))
        
        return Polynomial(result_coeffs)
    
    def sub_qq_q(self, other: Rational) -> Polynomial:
        """
        Вычитание рационального числа (свободного члена) из многочлена
        """
        result_coeffs = self.coefficients[:]
        result_coeffs[0] = result_coeffs[0].sub_qq_q(other)
        return Polynomial(result_coeffs)
    
    # P-3: Умножение многочлена на рациональное число
    def mul_pq_p(self, other: Rational) -> Polynomial:
        """
        Умножение многочлена на рациональное число
        """
        result_coeffs = []
        for coeff in self.coefficients:
            result_coeffs.append(coeff.mul_qq_q(other))
        
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
        if not self.coefficients or all(str(coeff.num) == "0" for coeff in self.coefficients):
            return Rational("0", "1")
        # Находим последний ненулевой коэффициент
        for i in range(len(self.coefficients) - 1, -1, -1):
            if str(self.coefficients[i].num) != "0":
                return self.coefficients[i]
        return Rational("0", "1")
    
    # P-6: Степень многочлена
    def deg_p_n(self) -> Natural:
        """
        Степень многочлена
        """
        if not self.coefficients or all(str(coeff.num) == "0" for coeff in self.coefficients):
            return Natural("0")
        
        # Находим последний ненулевой коэффициент
        for i in range(len(self.coefficients) - 1, -1, -1):
            if str(self.coefficients[i].num) != "0":
                return Natural(str(i))
        return Natural("0")
    
    # P-7: Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def fac_p_q(self) -> Rational:
        """
        Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
        """
        if not self.coefficients or all(str(coeff.num) == "0" for coeff in self.coefficients):
            return Rational("0", "1")
        
        # Собираем числители и знаменатели
        numerators = []
        denominators = []
        
        for coeff in self.coefficients:
            if str(coeff.num) != "0":
                # Преобразуем числитель и знаменатель в целые числа
                numerator_int = coeff.num  # используем напрямую Integer из Rational
                denominator_nat = coeff.den  # используем напрямую Natural из Rational
                
                # Берем модуль числителя, чтобы получить положительное значение для НОД
                numerator_abs = numerator_int.abs()
                numerators.append(numerator_abs.to_natural())
                denominators.append(denominator_nat)
        
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
                result_coeffs[i + j] = result_coeffs[i + j].add_qq_q(coeff1.mul_qq_q(coeff2))
        
        return Polynomial(result_coeffs)
    
    # P-9: Частное от деления многочлена на многочлен при делении с остатком
    def div_pp_p(self, other: Polynomial) -> Polynomial:
        """
        Частное от деления многочлена на многочлен при делении с остатком
        """
        if not other.coefficients or str(other.led_p_q().num) == "0":
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
        # Копируем коэффициенты для делимого
        dividend = Polynomial(self.coefficients[:])
        divisor = Polynomial(other.coefficients[:])
        
        # Если степень делимого меньше степени делителя, результат 0
        if dividend.deg_p_n().__lt__(divisor.deg_p_n()):
            return Polynomial([Rational("0", "1")])
        
        # Создаем результат (частное)
        quotient_coeffs = [Rational("0", "1")] * (int(str(dividend.deg_p_n())) - int(str(divisor.deg_p_n())) + 1)
        
        # Выполняем деление
        while not dividend.deg_p_n().__lt__(divisor.deg_p_n()) and str(dividend.led_p_q().num) != "0":
            # Находим степень текущего члена частного
            power_diff = int(str(dividend.deg_p_n())) - int(str(divisor.deg_p_n()))
            
            # Находим коэффициент текущего члена частного
            lead_dividend = dividend.led_p_q()
            lead_divisor = divisor.led_p_q()
            coeff_quotient = lead_dividend.div_qq_q(lead_divisor)
            
            # Добавляем коэффициент в частное
            quotient_coeffs[power_diff] = quotient_coeffs[power_diff].add_qq_q(coeff_quotient)
            
            # Создаем многочлен для вычитания
            subtrahend = divisor.mul_pq_p(coeff_quotient).mul_pxk_p(Natural(str(power_diff)))
            
            # Вычитаем из делимого
            dividend = dividend.sub_pp_p(subtrahend)
        
        return Polynomial(quotient_coeffs)
    
    # P-10: Остаток от деления многочлена на многочлен при делении с остатком
    def mod_pp_p(self, other: Polynomial) -> Polynomial:
        """
        Остаток от деления многочлена на многочлен при делении с остатком
        """
        if not other.coefficients or str(other.led_p_q().num) == "0":
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
    # P-10: Остаток от деления многочлена на многочлен при делении с остатком
    def mod_pp_p(self, other: Polynomial) -> Polynomial:
        """
        Остаток от деления многочлена на многочлен при делении с остатком
        """
        if not other.coefficients or str(other.led_p_q().num) == "0":
            raise ZeroDivisionError("Деление на нулевой многочлен")
        
        # Вычисляем частное
        quotient = self.div_pp_p(other)
        
        # Вычисляем произведение частного и делителя
        product = quotient.mul_pp_p(other)
        
        # Вычисляем остаток как разность делимого и произведения
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
        if str(lead_coeff.num) != "0":
            # Делим все коэффициенты на старший коэффициент, чтобы сделать его равным 1
            normalized_coeffs = []
            for coeff in a.coefficients:
                normalized_coeffs.append(coeff.div_qq_q(lead_coeff))
            return Polynomial(normalized_coeffs)
        else:
            return Polynomial([Rational("0", "1")])
    
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
            degree_rational = Rational(str(i), "1")
            new_coeff = coeff.mul_qq_q(degree_rational)
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
        if str(derivative.led_p_q().num) == "0":
            return Polynomial(self.coefficients[:])
        
        gcd_poly = self.gcf_pp_p(derivative)
        
        # Если НОД - нулевой многочлен, возвращаем копию исходного многочлена
        if str(gcd_poly.led_p_q().num) == "0":
            return Polynomial(self.coefficients[:])
        
        # Делим многочлен на НОД с его производной
        result = self.div_pp_p(gcd_poly)
        
        return result
    
    