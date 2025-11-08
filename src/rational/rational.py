from src.integer.integer import Integer
from src.natural.natural import Natural


class Rational:
    """
    Базовый класс для рациональных чисел num/den.

    num: Integer  (целое, может быть отрицательным или 0)
    den: Natural  (натуральное > 0)
    """

    def __init__(self, num: str = "0", den: str = "1"):
        self.set(num, den)

    def set(self, num: str, den: str):
        self.num = Integer(num)
        self.den = Natural(den)

        if int(self.den.value) == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

    def __str__(self) -> str:
        return f"{self.num.value}/{self.den.value}"
