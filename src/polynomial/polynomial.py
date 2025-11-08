from __future__ import annotations
from typing import List
from src.integer import Integer
from src.rational import Rational

class Polynomial:
    """Класс для многочленов с рациональными коэффициентами"""

    # [коэффициент, ...]
    # [1, 2, 3] -> 1*x^2 + 2*x^1 + 3*x^0
    # Степень многочлена равна len(coefficients) - 1
    # Коэффициенты хранятся как Rational для общности.
    coefficients: List[Rational]

    def __init__(self, value: List[Integer | Rational | str] | None = None):
        if value is None:
            self.coefficients = [Rational.from_int(Integer("0"))]
            return

        # Преобразуем все коэффициенты в Rational
        rational_coeffs = []
        for item in value:
            if isinstance(item, Rational):
                rational_coeffs.append(item)
            elif isinstance(item, Integer):
                rational_coeffs.append(Rational.from_int(item))
            elif isinstance(item, str):
                rational_coeffs.append(Rational.from_int(Integer(item)))
            else:
                raise TypeError(f"Неподдерживаемый тип коэффициента: {type(item)}")

        # Убираем ведущие нули
        first_non_zero = 0
        while first_non_zero < len(rational_coeffs) - 1 and rational_coeffs[first_non_zero].is_zero():
            first_non_zero += 1
        
        self.coefficients = rational_coeffs[first_non_zero:]

    def __str__(self) -> str:
        """Возвращает строковое представление многочлена"""
        if self.is_zero():
            return "0"

        res = []
        degree = len(self.coefficients) - 1
        for i, coeff in enumerate(self.coefficients):
            if coeff.is_zero():
                continue

            power = degree - i
            
            # Знак
            sign = ""
            if not res: # Первый член
                if coeff.num.is_negative():
                    sign = "-"
            else:
                sign = " - " if coeff.num.is_negative() else " + "

            abs_coeff = abs(coeff)

            # Коэффициент
            if abs_coeff.is_one() and power != 0:
                coeff_str = ""
            else:
                coeff_str = str(abs_coeff)

            # Переменная и степень
            if power > 1:
                power_str = f"x^{power}"
            elif power == 1:
                power_str = "x"
            else:
                power_str = ""
            
            # Собираем все вместе
            res.append(f"{sign}{coeff_str}{power_str}")

        return "".join(res)
    
    def __eq__(self, other: Polynomial) -> bool:
        """Проверяет равенство двух многочленов"""
        return self.coefficients == other.coefficients

    def is_zero(self) -> bool:
        """Проверяет, является ли многочлен нулевым"""
        return len(self.coefficients) == 1 and self.coefficients[0].is_zero()

    @staticmethod
    def from_string(s: str) -> Polynomial:
        """Создает многочлен из строки"""
        # TODO: Реализовать парсинг строки
        if s == "0":
            return Polynomial()
        # Простая реализация для примера
        parts = s.split('x')
        if len(parts) == 1:
            return Polynomial([Integer(parts[0])])
        
        # Это очень упрощенный парсер и он не будет работать для большинства случаев.
        # Правильная реализация требует разбора сложных выражений.
        # Например, "x^2 + 2x - 3"
        raise NotImplementedError("Парсинг многочленов из строки еще не реализован.")
