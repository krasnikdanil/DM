from src.integer.integer import Integer


""" Вычетание только целое на целое """
class Subzz(Integer):
    def sub_zz_z(self, other):
        if not isinstance(other, Integer):
            raise TypeError("Аргумент должен быть целым числом")
        result = int(self.value) - int(other.value)
        return str(result)
