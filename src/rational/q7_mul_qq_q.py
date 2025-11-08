from src.rational.rational import Rational
from src.rational.q1_red_q_q import Redqq
from src.integer.integer import Integer
from src.integer.z8_mul_zz_z import Mulzz


class Mulqqq(Rational):
    """
    Q-7: MUL_QQ_Q

    Умножение рациональных:
      (a/b) * (c/d) = (a*c) / (b*d)
    Потом RED_Q_Q.
    """

    def mul_qq_q(self, other: "Rational") -> Redqq:
        a = int(self.num.value)
        b = int(self.den.value)
        c = int(other.num.value)
        d = int(other.den.value)

        if b == 0 or d == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        num_str = Mulzz(str(a)).mul_zz_z(Integer(str(c)))
        den_val = b * d
        den_str = str(den_val)

        return Redqq(num_str, den_str).red_q_q()
