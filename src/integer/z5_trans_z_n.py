from src.integer.integer import Integer
from src.natural.natural import Natural

""" Целое число преобразуем в натуральное """
class Transzn(Integer):
    if self.value[0] == '-':
        raise ValueError("Отрицательное число не может стать N")
    if self.value == '0':
        raise ValueError("0 не может стать N")
    else:
        return Natural(self.value)
