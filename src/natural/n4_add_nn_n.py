from src.natural.natural import Natural


class NaturalAddition(Natural):
    """Дочерний класс для сложения натуральных чисел"""

    def add(self, other: 'Natural') -> 'NaturalAddition':
        """Сложение натуральных чисел"""
        result = int(self.value) + int(other.value)
        return NaturalAddition(str(result))