from src.natural.natural import Natural


#НОД натуральных чисел
class Gcfnnn(Natural):
    def gcf_nn_n(self,other: 'Natural') -> str:
        a, b = int(self.value), int(other.value)
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a

        return str(a + b)
