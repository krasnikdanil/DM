from src.integer.integer import Integer

""" Определяем знак целого числа и является ли оно 0 """
class Poz(Integer):
    def poz_z_d(self) -> str:
        if '0' == self.value:
            return '0'
        if abs(int(self.value)) == int(self.value):
            return "1"
        if abs(int(self.value)) != int(self.value):
            return "-1"
        
