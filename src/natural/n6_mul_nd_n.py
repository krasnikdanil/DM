from src.natural.natural import Natural


class NaturalMultiplyByDigit(Natural):
    """Дочерний класс для умножения натурального числа на цифру"""

    def multiply_by_digit(self, digit: str) -> 'NaturalMultiplyByDigit':
        """Умножение натурального числа на цифру"""
        if len(digit) != 1 or not digit.isdigit():
            raise ValueError("Аргумент должен быть одной цифрой")

        if int(digit) == 0:
            return NaturalMultiplyByDigit("0")

        result = int(self.value) * int(digit)
        return NaturalMultiplyByDigit(str(result))