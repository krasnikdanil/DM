from src.natural.natural import Natural

# Вычитание из первого большего натурального числа второго меньшего или равного
class Subnnn(Natural):
    def sub_nn_n(self, other: 'Natural') -> str:
        a = int(self.value)
        b = int(other.value)
        if a >= b:
            return str(a-b)
        else:
            return str(b-a)