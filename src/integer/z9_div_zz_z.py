from src.integer.integer import Integer


""" Деление только целое на целое """
class Divzz(Integer):
    def div_zz_z(self, other):
        if not isinstance(other, Integer):
            raise TypeError("Аргумент должен быть целым числом")
        if int(other.value) == 0:
            raise ZeroDivisionError("Делить на 0 нельзя")
        result = int(int(self.value) / int(other.value))  # целочисленное деление
        return str(result)
