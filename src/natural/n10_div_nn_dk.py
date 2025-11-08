from src.natural.natural import Natural


class NaturalFirstDivisionDigit(Natural):
    """Дочерний класс для вычисления первой цифры деления с позицией"""

    def first_division_digit(self, other: 'Natural') -> 'NaturalFirstDivisionDigit':
        """Вычисление первой цифры деления большего на меньшее, домноженное на 10^k"""
        num1 = int(self.value)
        num2 = int(other.value)

        if num2 == 0:
            raise ValueError("Деление на ноль невозможно")

        # Определяем большее и меньшее числа
        dividend = max(num1, num2)  # делимое (большее)
        divisor = min(num1, num2)  # делитель (меньшее)

        # Находим первую цифру деления
        first_digit = dividend // divisor

        # Находим k - позицию цифры (считая с нуля)
        k = 0
        temp = first_digit
        while temp >= 10:
            temp //= 10
            k += 1

        # Домножаем на 10^k
        result = first_digit * (10 ** k)

        return NaturalFirstDivisionDigit(str(result))