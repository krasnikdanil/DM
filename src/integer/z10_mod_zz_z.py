from src.integer.integer import Integer


""" Остаток от деления только целое на целое """
class Modzz(Integer):
    def mod_zz_z(self, other):
        if not isinstance(other, Integer):
            raise TypeError("Аргумент должен быть целым числом")
        if int(other.value) == 0:
            raise ZeroDivisionError("Нельзя делить на ноль")
        result = int(self.value) % int(other.value)
        return str(result)
