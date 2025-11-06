from src.integer.integer import Integer


""" Сложение только для целое на целое """
class Addzz(Integer):
    def add_zz_z(self, other):
        if not isinstance(other, Integer):
            raise TypeError("Аргумент должен быть целым числом")
        result = int(self.value) + int(other.value)
        return str(result)
