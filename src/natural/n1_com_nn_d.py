from src.natural.natural import Natural

class NaturalComparison(Natural):
    """Дочерний класс для сравнения натуральных чисел"""

    def compare(self, other: 'Natural') -> int:
        """Сравнение натуральных чисел: 1 - если первое больше второго, 0 - если равно, -1 - иначе"""
        if int(self.value) > int(other.value):
            return 1
        elif int(self.value) == int(other.value):
            return 0
        else:
            return -1