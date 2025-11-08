from src.rational.rational import Rational
from src.rational.q1_red_q_q import Redqq


class Intqb(Rational):
    """
    Q-2: INT_Q_B

    Проверка, является ли рациональное число целым.
    Возвращает True, если после сокращения знаменатель = 1.
    """

    def int_q_b(self) -> bool:
        reduced = Redqq(self.num.value, self.den.value).red_q_q()
        return int(reduced.den.value) == 1
