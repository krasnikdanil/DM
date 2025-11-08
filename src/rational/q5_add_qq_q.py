from src.rational.rational import Rational
from src.rational.q1_red_q_q import Redqq
from src.integer.integer import Integer
from src.integer.z6_add_zz_z import Addzz
from src.integer.z8_mul_zz_z import Mulzz
from src.natural.natural import Natural
from src.natural.n14_lcm_nn_n import NaturalLCM  


class Addqqq(Rational):
    """
    Q-5: ADD_QQ_Q

    Сложение двух рациональных чисел:
      (a/b) + (c/d) = (a * (L/b) + c * (L/d)) / L,
    где L = LCM(b, d).

    После вычисления результат сокращается через RED_Q_Q.
    """

    def add_qq_q(self, other: "Rational") -> Redqq:
        a = int(self.num.value)
        b = int(self.den.value)
        c = int(other.num.value)
        d = int(other.den.value)

        if b == 0 or d == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        lcm_obj = NaturalLCM(str(b)).lcm(Natural(str(d)))
        lcm_val = int(lcm_obj.value)

        k1 = lcm_val // b
        k2 = lcm_val // d

        a_k1 = Mulzz(str(a)).mul_zz_z(Integer(str(k1)))  # str
        c_k2 = Mulzz(str(c)).mul_zz_z(Integer(str(k2)))  # str

        new_num = Addzz(a_k1).add_zz_z(Integer(c_k2))    # str
        new_den = str(lcm_val)

        return Redqq(new_num, new_den).red_q_q()
