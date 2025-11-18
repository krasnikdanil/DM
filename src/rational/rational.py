from natural.natural import Natural
from integer.integer import Integer


class Rational:
    """
    Рациональное число вида num / den.

    num — целое (Integer, может быть отрицательным или нулём),
    den — натуральное (Natural, строго > 0).

    Реализует операции из блока Q (Коллоквиум ДМ):

      Q-1: RED_Q_Q   -> red_q_q()
      Q-2: INT_Q_B   -> int_q_b()
      Q-3: TRANS_Z_Q -> trans_z_q()
      Q-4: TRANS_Q_Z -> trans_q_z()
      Q-5: ADD_QQ_Q  -> add_qq_q()
      Q-6: SUB_QQ_Q  -> sub_qq_q()
      Q-7: MUL_QQ_Q  -> mul_qq_q()
      Q-8: DIV_QQ_Q  -> div_qq_q()
    """

    def __init__(self, num: str = "0", den: str = "1"):
        self.set(num, den)

    # ================= Базовая инициализация =================

    def set(self, num: str, den: str):
        """
        Устанавливает числитель и знаменатель с проверкой:
        - знаменатель != 0
        - знак хранится только в числителе
        """
        self.num = Integer(num)
        self.den = Natural(den)

        # Natural у вас допускает "0", поэтому явно запрещаем
        if str(self.den) == "0":
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        # на всякий случай нормализуем знак: знаменатель всегда > 0
        # (Natural не поддерживает '-', так что тут только защита от "0")
        # если когда-то добавите отрицательный den — переносите знак сюда.

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    # ================== Q-1: RED_Q_Q ==================

    def red_q_q(self) -> "Rational":
        """
        Q-1: RED_Q_Q
        Сокращение дроби до несократимого вида.
        """
        # Если числитель 0, возвращаем 0/1
        if self.num.is_zero():
            return Rational("0", "1")

        # Находим НОД числителя и знаменателя
        # abs(self.num) вернет Natural
        common_divisor = abs(self.num).gcd(self.den)

        # Сокращаем числитель и знаменатель
        new_num = self.num // Integer(str(common_divisor))
        new_den = self.den // common_divisor

        res = Rational()
        res.num = new_num
        res.den = new_den
        return res

    # ================== Q-2: INT_Q_B ==================

    def int_q_b(self) -> bool:
        """
        Q-2: INT_Q_B
        Проверка: является ли рациональное число целым.
        True, если после сокращения знаменатель = 1.
        """
        r = self.red_q_q()
        return str(r.den) == "1"

    # ================== Q-3: TRANS_Z_Q ==================

    @staticmethod
    def trans_z_q(z: Integer) -> "Rational":
        """
        Q-3: TRANS_Z_Q
        Преобразование целого в рациональное: z -> z/1.
        """
        if not isinstance(z, Integer):
            raise TypeError("Ожидается Integer")
        return Rational(str(z), "1")

    # ================== Q-4: TRANS_Q_Z ==================

    def trans_q_z(self) -> Integer:
        """
        Q-4: TRANS_Q_Z
        Преобразование рационального в целое.
        Разрешено только если после RED_Q_Q знаменатель = 1.
        """
        r = self.red_q_q()
        if str(r.den) != "1":
            raise ValueError("Рациональное число не является целым")
        return Integer(str(r.num))

    # ================== Q-5: ADD_QQ_Q ==================

    def add_qq_q(self, other: "Rational") -> "Rational":
        """
        Q-5: ADD_QQ_Q
        Сложение двух рациональных чисел.
        """
        if not isinstance(other, Rational):
            raise TypeError("Складывать можно только с Rational")

        # Общий знаменатель - НОК
        common_den = self.den.lcm(other.den)

        # Дополнительные множители
        k1 = common_den // self.den
        k2 = common_den // other.den

        # Новый числитель
        new_num = self.num * Integer(str(k1)) + other.num * Integer(str(k2))

        # Создаем результат и сокращаем
        result = Rational()
        result.num = new_num
        result.den = common_den
        return result.red_q_q()

    # ================== Q-6: SUB_QQ_Q ==================

    def sub_qq_q(self, other: "Rational") -> "Rational":
        """
        Q-6: SUB_QQ_Q
        Вычитание рациональных чисел.
        """
        if not isinstance(other, Rational):
            raise TypeError("Вычитать можно только Rational")

        # Общий знаменатель - НОК
        common_den = self.den.lcm(other.den)

        # Дополнительные множители
        k1 = common_den // self.den
        k2 = common_den // other.den

        # Новый числитель
        new_num = self.num * Integer(str(k1)) - other.num * Integer(str(k2))

        # Создаем результат и сокращаем
        result = Rational()
        result.num = new_num
        result.den = common_den

        return result.red_q_q()

    # ================== Q-7: MUL_QQ_Q ==================

    def mul_qq_q(self, other: "Rational") -> "Rational":
        """
        Q-7: MUL_QQ_Q
        Умножение рациональных чисел.
        """
        if not isinstance(other, Rational):
            raise TypeError("Умножать можно только Rational")

        # Новый числитель и знаменатель
        new_num = self.num * other.num
        new_den = self.den * other.den

        # Создаем результат и сокращаем
        result = Rational()
        result.num = new_num
        result.den = new_den
        return result.red_q_q()

    # ================== Q-8: DIV_QQ_Q ==================

    def div_qq_q(self, other: "Rational") -> "Rational":
        """
        Q-8: DIV_QQ_Q
        Деление рациональных чисел.
        """
        if not isinstance(other, Rational):
            raise TypeError("Делить можно только на Rational")

        if other.num.is_zero():
            raise ZeroDivisionError("Деление на ноль: числитель второго числа равен 0")

        # "Переворачиваем" вторую дробь и умножаем
        # Знак числителя второй дроби
        new_num = self.num * Integer(str(other.den))
        new_den = self.den * abs(other.num)

        # Учитываем знак числителя второй дроби
        if other.num.is_negative():
            new_num = -new_num

        # Создаем результат и сокращаем
        result = Rational()
        result.num = new_num
        result.den = new_den
        return result.red_q_q()

    # ========= Дополнительно: операторы для удобства =========

    def __add__(self, other: "Rational") -> "Rational":
        return self.add_qq_q(other)

    def __sub__(self, other: "Rational") -> "Rational":
        return self.sub_qq_q(other)

    def __mul__(self, other: "Rational") -> "Rational":
        return self.mul_qq_q(other)

    def __truediv__(self, other: "Rational") -> "Rational":
        return self.div_qq_q(other)
