from src.rational.rational import Rational
from src.rational.q2_int_q_b import Intqb
from src.integer.integer import Integer


class Transqz(Rational):
    """
    Q-4: TRANS_Q_Z

    Преобразование рационального числа в целое.
    Допустимо только если после сокращения знаменатель = 1.
    """

    def trans_q_z(self) -> Integer:
        if not Intqb(self.num.value, self.den.value).int_q_b():
            raise ValueError("Рациональное число не является целым")
        return Integer(self.num.value)