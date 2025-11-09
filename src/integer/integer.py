from natural.natural import Natural

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

        # Реализация через сложение с отрицательным числом (a - b = a + (-b))
        # Это корректный и простой способ, использующий уже реализованные методы.
        negated_other = -other # используем существующий __neg__
        result = self + negated_other # используем существующий __add__
        return result

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
    
    """ Деление Integer (округление к нулю) """
    def __floordiv__(self, other: Integer) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError("Деление возможно только на целое число")
        if str(other) == "0":
            raise ZeroDivisionError("Деление на ноль")

        # Получаем модули (Natural) для деления
        self_abs = Natural(str(self))
        other_abs = Natural(str(other))

        quotient_natural = self_abs // other_abs # Natural.__floordiv__
        remainder_natural = self_abs % other_abs # Natural.__mod__
        
        quotient = Integer(str(quotient_natural))
        quotient.sign = self.sign * other.sign

        # Коррекция для усеченного деления (округление к нулю).
        # Если делимое и делитель имеют разные знаки и остаток от деления не равен нулю,
        # результат нужно скорректировать, чтобы он был ближе к нулю.
        # Например: -7 // 3 = -3 (floor), но -7 trunc_div 3 = -2 (trunc).
        # Или: 7 // -3 = -3 (floor), но 7 trunc_div -3 = -2 (trunc).
        if (self.sign != other.sign) and str(remainder_natural) != "0":
             quotient = quotient - Integer("1") # вычитаем 1 (с тем же знаком, что и частное до коррекции)

        return quotient

    """ Остаток от деления Integer """
    def __mod__(self, other: Integer) -> Integer:
        if not isinstance(other, Integer):
            raise TypeError("Деление возможно только на целое число")
        if str(other) == "0":
            raise ZeroDivisionError("Деление на ноль")
        # a % n = a - n * (a // n)
        quotient = self // other # результат Integer
        # Умножение other * quotient может вызвать ошибку, если super().__mul__ в __mul__ получит Integer вместо Natural.
        # Нужно вычислить n * (a // n) используя Natural числа.
        n_nat = Natural(str(other))
        q_nat = Natural(str(quotient))
        product_nat = n_nat * q_nat # Natural.__mul__
        product_int = Integer(str(product_nat))
        product_int.sign = other.sign * quotient.sign # Устанавливаем знак результата умножения

        remainder = self - product_int # Integer.__sub__
        
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

    
    

