from src.integer.integer import Integer
from src.natural.natural import Natural

""" Натуральное число преобразуем в целое"""
class Transnz(Natural):
    def trans_n_z(self):
        return Integer(self.value)
