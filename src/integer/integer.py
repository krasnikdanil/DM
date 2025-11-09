from src.natural.natural import Natural

class Integer(Natural):
    def __init__(self, value: str = "0"):
        if not isinstance(value, str):
            raise TypeError("Аргумент должен быть строкой")

        if value.startswith('-'):
            self.sign = -1
            super().__init__(value[1:])
        else:
            self.sign = 1
            if value.startswith('+'):
                super().__init__(value[1:])
            else:
                super().__init__(value)

    def __str__(self):
        if self.sign == -1 and (len(self.values) > 1 or self.values[0] != 0):
            return "-" + super().__str__()
        return super().__str__()

    def __neg__(self):
        if str(self) == "0":
            return self
        
        negated_int = Integer(str(self))
        negated_int.sign = -self.sign
        return negated_int

    """" Сложение Integer """
    def __add__(self, other: Integer) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError("Сложение возможно только с целыми числами")
        # Если знаки одинаковые
        if self.sign == other.sign:
            result_natural = super().__add__(other)
            result = Integer(str(result_natural))
            result.sign = self.sign
            return result
        # Если знаки разные
        else:
            # Сравниваем по модулю
            if super().__gt__(other): # self > other
                result_natural = super().__sub__(other)
                result = Integer(str(result_natural))
                result.sign = self.sign
            elif super().__lt__(other): # self < other
                result_natural = other.__sub__(self)
                result = Integer(str(result_natural))
                result.sign = other.sign
            else: # self == other
                result = Integer("0")
            
            return result
    
    """ Вычитание Integer """
    def __sub__(self, other: Integer) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError("Вычитание возможно только для целых чисел")
        
        return self + (-other)

    """ Умножение Integer """
    def __mul__(self, other: Integer) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError("Умножение возможно только на целое число")

        if str(self) == "0" or str(other) == "0":
            return Integer("0")

        result_natural = super().__mul__(other)
        result = Integer(str(result_natural))
        result.sign = self.sign * other.sign
        return result
    
    """ Деление Integer """
    def __floordiv__(self, other: Integer) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError("Деление возможно только на целое число")
        if str(other) == "0":
            raise ZeroDivisionError("Деление на ноль")

        quotient_natural = super().__floordiv__(other)
        remainder_natural = super().__mod__(other)
        
        quotient = Integer(str(quotient_natural))
        quotient.sign = self.sign * other.sign

        # Коррекция для отрицательных результатов с остатком
        if quotient.sign == -1 and str(remainder_natural) != "0":
            quotient = quotient + Integer("-1")
            
        return quotient

    """ Остаток от деления Integer """
    def __mod__(self, other: Integer) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError("Деление возможно только на целое число")
        if str(other) == "0":
            raise ZeroDivisionError("Деление на ноль")
        # a % n = a - n * (a // n)
        quotient = self // other
        product = other * quotient
        remainder = self - product
        
        return remainder

    """ Возвращает абсолютное значение числа (модуль)
     как натуральное число. """
    def __abs__(self) -> Natural:
        return Natural(super().__str__())

    """ Определение знака числа.
        Возвращает:
        1 - если число положительное
        -1 - если число отрицательное
        0 - если число ноль """
    def poz(self) -> int:
        if self.values == [0]:
            return 0
        elif self.sign == 1:
            return 1
        else:
            return -1

    """Преобразует натуральное число в целое."""
    @staticmethod
    def from_natural(natural: Natural) -> Integer:
        if not isinstance(natural, Natural):
            raise TypeError("Аргумент должен быть натуральным числом")
        return Integer(str(natural))

    """ Преобразует целое неотрицательное число в натуральное.
        Вызывает ValueError, если число отрицательное. """
    def to_natural(self) -> Natural:
        if self.sign == -1 and str(self) != "0":
            raise ValueError("Нельзя преобразовать отрицательное число в натуральное")
        return Natural(str(self))

    
    

