from src.natural.natural import Natural
import math


class NaturalLCM(Natural):
    """Дочерний класс для вычисления НОК натуральных чисел"""

    def lcm(self, other: 'Natural') -> 'NaturalLCM':
        """НОК натуральных чисел"""
        num1 = int(self.value)
        num2 = int(other.value)

        if num1 == 0 or num2 == 0:
            raise ValueError("НОК не определен для нуля")

        result = abs(num1 * num2) // math.gcd(num1, num2)

        return NaturalLCM(str(result))