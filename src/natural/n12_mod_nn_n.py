from src.natural.natural import Natural


class NaturalModulo(Natural):
    """Дочерний класс для вычисления остатка от деления натуральных чисел"""

    def modulo(self, other: 'Natural') -> 'NaturalModulo':
        """Остаток от деления первого натурального числа на второе"""
        num1 = int(self.value)
        num2 = int(other.value)

        if num2 == 0:
            raise ValueError("Деление на ноль невозможно")

        result = num1 % num2
        return NaturalModulo(str(result))