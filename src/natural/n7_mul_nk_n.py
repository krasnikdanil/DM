from src.natural.natural import Natural

# Умножение натурального числа на 10^k, k-натуральное (не длинное)
class Mulnkn(Natural):
    def mul_nk_n(self,k: 'Natural') -> str:
        if int(k.value) > 100:
            raise ValueError("k не должен превышать 100")
        result = str(int(self.value) * 10 ** int(k.value))
        return result