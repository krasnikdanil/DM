from src.integer.integer import Integer

""" Абсолютная величина числа, результат - натуральное """
class Abszn(Integer):
    def abs_z_n(self) -> str:
        if int(self.value) == 0:
            raise ValueError("0 не является N числом")
        else:
            return str(abs(int(self.value)))
