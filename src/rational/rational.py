from src.natural.natural import Natural
from src.integer.integer import Integer


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

        - Переносит знак в числитель (den > 0).
        - Делит num и den на НОД(|num|, den).
        - 0 представляется как 0/1.
        """
        num_int = int(str(self.num))
        den_int = int(str(self.den))

        if den_int == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        # 0/x -> 0/1
        if num_int == 0:
            return Rational("0", "1")

        # |num| и den как Natural
        abs_num_nat = abs(Integer(str(self.num)))          # Natural
        den_nat = Natural(str(self.den))

        # НОД через Natural.gcd
        gcd_nat = abs_num_nat.gcd(den_nat)
        gcd_int = int(str(gcd_nat))

        if gcd_int <= 0:
            gcd_int = 1

        # Делим на НОД (через int; допускается, т.к. это поверх ваших N/Z)
        new_num_int = num_int // gcd_int
        new_den_int = den_int // gcd_int

        # Нормализуем знак: знаменатель > 0, знак только в числителе
        if new_den_int < 0:
            new_den_int = -new_den_int
            new_num_int = -new_num_int

        # Защита от -0
        if new_num_int == 0:
            return Rational("0", "1")

        return Rational(str(new_num_int), str(new_den_int))

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
        Сложение двух рациональных чисел:
          (a/b) + (c/d) = (a*(L/b) + c*(L/d)) / L,
        где L = НОК(b, d).
        Результат сокращается через RED_Q_Q.
        """
        if not isinstance(other, Rational):
            raise TypeError("Складывать можно только с Rational")

        r1 = self.red_q_q()
        r2 = other.red_q_q()

        a = int(str(r1.num))
        b = int(str(r1.den))
        c = int(str(r2.num))
        d = int(str(r2.den))

        if b == 0 or d == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        # НОК знаменателей через Natural.lcm
        L = int(str(Natural(str(b)).lcm(Natural(str(d)))))

        k1 = L // b
        k2 = L // d

        num = a * k1 + c * k2
        den = L

        return Rational(str(num), str(den)).red_q_q()

    # ================== Q-6: SUB_QQ_Q ==================

    def sub_qq_q(self, other: "Rational") -> "Rational":
        """
        Q-6: SUB_QQ_Q
        Вычитание рациональных:
          (a/b) - (c/d) = (a*(L/b) - c*(L/d)) / L,
        где L = НОК(b, d).
        Результат сокращается через RED_Q_Q.
        """
        if not isinstance(other, Rational):
            raise TypeError("Вычитать можно только Rational")

        r1 = self.red_q_q()
        r2 = other.red_q_q()

        a = int(str(r1.num))
        b = int(str(r1.den))
        c = int(str(r2.num))
        d = int(str(r2.den))

        if b == 0 or d == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        L = int(str(Natural(str(b)).lcm(Natural(str(d)))))

        k1 = L // b
        k2 = L // d

        num = a * k1 - c * k2
        den = L

        return Rational(str(num), str(den)).red_q_q()

    # ================== Q-7: MUL_QQ_Q ==================

    def mul_qq_q(self, other: "Rational") -> "Rational":
        """
        Q-7: MUL_QQ_Q
        Умножение рациональных чисел:
          (a/b) * (c/d) = (a*c) / (b*d)
        Результат сокращается через RED_Q_Q.
        """
        if not isinstance(other, Rational):
            raise TypeError("Умножать можно только Rational")

        r1 = self.red_q_q()
        r2 = other.red_q_q()

        a = int(str(r1.num))
        b = int(str(r1.den))
        c = int(str(r2.num))
        d = int(str(r2.den))

        if b == 0 or d == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        num = a * c
        den = b * d

        if den == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        return Rational(str(num), str(den)).red_q_q()

    # ================== Q-8: DIV_QQ_Q ==================

    def div_qq_q(self, other: "Rational") -> "Rational":
        """
        Q-8: DIV_QQ_Q
        Деление рациональных чисел:
          (a/b) / (c/d) = (a*d) / (b*c), при c != 0.
        Результат сокращается через RED_Q_Q.
        """
        if not isinstance(other, Rational):
            raise TypeError("Делить можно только на Rational")

        r1 = self.red_q_q()
        r2 = other.red_q_q()

        a = int(str(r1.num))
        b = int(str(r1.den))
        c = int(str(r2.num))
        d = int(str(r2.den))

        if b == 0 or d == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")
        if c == 0:
            raise ZeroDivisionError("Деление на ноль: числитель второго числа равен 0")

        num = a * d
        den = b * c

        if den == 0:
            raise ZeroDivisionError("Знаменатель рационального числа не может быть 0")

        return Rational(str(num), str(den)).red_q_q()

    # ========= Дополнительно: операторы для удобства =========

    def __add__(self, other: "Rational") -> "Rational":
        return self.add_qq_q(other)

    def __sub__(self, other: "Rational") -> "Rational":
        return self.sub_qq_q(other)

    def __mul__(self, other: "Rational") -> "Rational":
        return self.mul_qq_q(other)

    def __truediv__(self, other: "Rational") -> "Rational":
        return self.div_qq_q(other)
