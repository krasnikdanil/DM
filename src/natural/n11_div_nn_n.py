from src.natural.natural import Natural


# Неполное частное от деления первого натурального числа на второе с 
# остатком (делитель отличен от нуля)
class Divnnn(Natural):
    def div_nn_n(self,other: 'Natural') -> str:
        if other.value == '0':
            raise ValueError("Делитель должен быть отличен от нуля")
        div = int(self.value) // int(other.value)
        rem = int(self.value) % int(other.value)
        return f"Частное: {div}; Остаток: {rem}"