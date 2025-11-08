from src.rational.rational import Rational
from src.integer.integer import Integer
from src.natural.natural import Natural

from src.integer.z1_abs_z_n import Abszn      # Z-1: ABS_Z_N
from src.natural.n13_gcf_nn_n import Gcfnnn   # N-13: GCF_NN_N
from src.integer.z9_div_zz_z import Divzz     # Z-9: DIV_ZZ_Z


class Redqq(Rational):
    """
    Q-1: RED_Q_Q — сокращение рационального числа до несократимого вида.

    self.num.value: целое (str)
    self.den.value: натуральное > 0 (str)

    Результат:
      - знаменатель > 0;
      - num и den поделены на НОД(|num|, den);
      - 0 представлен как 0/1.
    """

    def red_q_q(self) -> "Redqq":
        num_int = int(self.num.value)
        den_int = int(self.den.value)

        if den_int == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        if num_int == 0:
            return Redqq("0", "1")

        abs_num_str = Abszn(str(num_int)).abs_z_n()
        abs_num_nat = Natural(abs_num_str)

        gcd_str = Gcfnnn(abs_num_nat.value).gcf_nn_n(Natural(str(den_int)))
        try:
            gcd_int = int(gcd_str)
        except ValueError:
            gcd_int = 1
        if gcd_int <= 0:
            gcd_int = 1

        new_num_str = Divzz(str(num_int)).div_zz_z(Integer(str(gcd_int)))
        new_den_str = Divzz(str(den_int)).div_zz_z(Integer(str(gcd_int)))

        new_num_int = int(new_num_str)
        new_den_int = int(new_den_str)

        if new_den_int < 0:
            new_den_int = -new_den_int
            new_num_int = -new_num_int

        if new_num_int == 0:
            return Redqq("0", "1")

        return Redqq(str(new_num_int), str(new_den_int))