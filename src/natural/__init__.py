"""
Модуль для работы с натуральными числами
"""
from typing import List


class Natural:
    """
    Класс для представления натуральных чисел
    Число представляется в виде списка цифр в обратном порядке
    Например, число 1234 будет представлено как [4, 3, 2, 1]
    """
    
    def __init__(self, digits: List[int] = None):
        """
        Инициализация натурального числа
        :param digits: список цифр числа в обратном порядке
        """
        if digits is None:
            self.digits = [0]  # по умолчанию 0
        else:
            # Убираем ведущие нули
            while len(digits) > 1 and digits[-1] == 0:
                digits.pop()
            self.digits = digits[:]
    
    def __str__(self):
        """Строковое представление числа"""
        return ''.join(map(str, reversed(self.digits)))
    
    def __repr__(self):
        return f"Natural({self.digits})"
    
    def is_zero(self):
        """Проверяет, является ли число нулем"""
        return len(self.digits) == 1 and self.digits[0] == 0

    def copy(self):
        """Создает копию числа"""
        return Natural(self.digits[:])
