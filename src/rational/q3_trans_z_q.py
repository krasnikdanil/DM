from src.integer.integer import Integer
from src.rational.rational import Rational


class Transzq(Integer):
    """
    Q-3: TRANS_Z_Q

    Преобразование целого в рациональное: z -> z/1.
    """

    def trans_z_q(self) -> Rational:
        return Rational(self.value, "1")
