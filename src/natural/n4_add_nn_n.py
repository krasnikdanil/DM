from src.natural.natural import Natural


class NaturalAddition(Natural):
    """Дочерний класс для сложения натуральных чисел"""

    def __add__(self, other) -> str:
        """Сложение натуральных чисел"""
        if not isinstance(other, Natural):
            raise TypeError("Аргумент должен быть натуральным числом")
        result = int(self.value) + int(other.value)
        return result
