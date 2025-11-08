from src.rational.rational import Rational
from src.rational.q1_red_q_q import Redqq
from src.integer.integer import Integer
from src.integer.z8_mul_zz_z import Mulzz


class Divqqq(Rational):
    """
    Q-8: DIV_QQ_Q

    Деление рациональных:
      (a/b) / (c/d) = (a*d) / (b*c), при c != 0.
    Потом RED_Q_Q.
    """

    def div_qq_q(self, other: "Rational") -> Redqq:
        a = int(self.num.value)
        b = int(self.den.value)
        c = int(other.num.value)
        d = int(other.den.value)

        if b == 0 or d == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")
        if c == 0:
            raise ZeroDivisionError("Деление на ноль: числитель второго числа равен 0")

        num_str = Mulzz(str(a)).mul_zz_z(Integer(str(d)))
        den_val = b * c
        if den_val == 0:
            raise ZeroDivisionError("Деление на ноль в знаменателе результата")

        den_str = str(den_val)

        return Redqq(num_str, den_str).red_q_q()
