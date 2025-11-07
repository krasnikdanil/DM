from src.natural.natural import Natural


class NaturalMultiplication(Natural):
    """Дочерний класс для умножения натуральных чисел"""

    def multiply(self, other: 'Natural') -> 'NaturalMultiplication':
        """Умножение натуральных чисел"""
        result = int(self.value) * int(other.value)
        return NaturalMultiplication(str(result))