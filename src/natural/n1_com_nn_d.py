from src.natural.natural import Natural

# Сравниваем два числа: 1 - если первое больше второго, 0 - если равно, -1 - иначе
class Comnnd(Natural):
    def com_mm_d(self, other: 'Natural') -> str:
        if int(self.value) > int(other.value):
            return '1'
        elif int(self.value) == int(other.value):
            return '0'
        else:
            return '-1'
