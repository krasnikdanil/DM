from src.integer.integer import Integer


""" Умножение только целое на целое """
class Mulzz(Integer):
    def mul_zz_z(self, other):
        if not isinstance(other, Integer):
            raise TypeError("Аргумент должен быть целым числом")
        result = int(self.value) * int(other.value)
        return str(result)
