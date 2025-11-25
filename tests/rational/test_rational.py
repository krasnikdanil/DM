import pytest
from src.rational.rational import Rational
from src.integer.integer import Integer
from src.natural.natural import Natural

class TestRational:
    # Тесты для инициализации и строкового представления
    def test_init_and_str(self):
        r1 = Rational("1", "2")
        assert str(r1) == "1/2"

        r2 = Rational("0", "5")
        assert str(r2) == "0/5"

        r3 = Rational("-3", "4")
        assert str(r3) == "-3/4"

        with pytest.raises(ZeroDivisionError):
            Rational("1", "0")

    # Тесты для RED_Q_Q (сокращение дробей)
    def test_red_q_q(self):
        r1 = Rational("2", "4")
        assert str(r1.red_q_q()) == "1/2"

        r2 = Rational("10", "5")
        assert str(r2.red_q_q()) == "2/1"

        r3 = Rational("0", "100")
        assert str(r3.red_q_q()) == "0/1"

        r4 = Rational("-6", "9")
        assert str(r4.red_q_q()) == "-2/3"

        r5 = Rational("7", "1")
        assert str(r5.red_q_q()) == "7/1"

    # Тесты для INT_Q_B (проверка на целое число)
    def test_int_q_b(self):
        r1 = Rational("4", "2")
        assert r1.int_q_b() == True

        r2 = Rational("3", "2")
        assert r2.int_q_b() == False

        r3 = Rational("0", "1")
        assert r3.int_q_b() == True

        r4 = Rational("-8", "4")
        assert r4.int_q_b() == True

    # Тесты для TRANS_Z_Q (преобразование целого в рациональное)
    def test_trans_z_q(self):
        i1 = Integer("5")
        q1 = Rational.trans_z_q(i1)
        assert str(q1) == "5/1"

        i2 = Integer("-3")
        q2 = Rational.trans_z_q(i2)
        assert str(q2) == "-3/1"

        i3 = Integer("0")
        q3 = Rational.trans_z_q(i3)
        assert str(q3) == "0/1"

        with pytest.raises(TypeError):
            Rational.trans_z_q(Natural("5"))

    # Тесты для TRANS_Q_Z (преобразование рационального в целое)
    def test_trans_q_z(self):
        q1 = Rational("6", "2")
        assert str(q1.trans_q_z()) == "3"

        q2 = Rational("-10", "5")
        assert str(q2.trans_q_z()) == "-2"

        q3 = Rational("0", "7")
        assert str(q3.trans_q_z()) == "0"

        q4 = Rational("7", "1")
        assert str(q4.trans_q_z()) == "7"

        with pytest.raises(ValueError):
            Rational("3", "2").trans_q_z()

    # Тесты для ADD_QQ_Q (сложение)
    def test_add_qq_q(self):
        r1 = Rational("1", "2")
        r2 = Rational("1", "3")
        assert str(r1.add_qq_q(r2)) == "5/6"

        r3 = Rational("1", "4")
        r4 = Rational("3", "4")
        assert str(r3.add_qq_q(r4)) == "1/1"

        r5 = Rational("-1", "2")
        r6 = Rational("1", "2")
        assert str(r5.add_qq_q(r6)) == "0/1"

        r7 = Rational("2", "1")
        r8 = Rational("3", "1")
        assert str(r7.add_qq_q(r8)) == "5/1"

    # Тесты для SUB_QQ_Q (вычитание)
    def test_sub_qq_q(self):
        r1 = Rational("1", "2")
        r2 = Rational("1", "3")
        assert str(r1.sub_qq_q(r2)) == "1/6"

        r3 = Rational("3", "4")
        r4 = Rational("1", "4")
        assert str(r3.sub_qq_q(r4)) == "1/2"

        r5 = Rational("1", "2")
        r6 = Rational("1", "2")
        assert str(r5.sub_qq_q(r6)) == "0/1"

        r7 = Rational("2", "1")
        r8 = Rational("3", "1")
        assert str(r7.sub_qq_q(r8)) == "-1/1"

    # Тесты для MUL_QQ_Q (умножение)
    def test_mul_qq_q(self):
        r1 = Rational("1", "2")
        r2 = Rational("1", "3")
        assert str(r1.mul_qq_q(r2)) == "1/6"

        r3 = Rational("2", "3")
        r4 = Rational("3", "4")
        assert str(r3.mul_qq_q(r4)) == "1/2"

        r5 = Rational("0", "5")
        r6 = Rational("10", "1")
        assert str(r5.mul_qq_q(r6)) == "0/1"

        r7 = Rational("-1", "2")
        r8 = Rational("1", "3")
        assert str(r7.mul_qq_q(r8)) == "-1/6"

    # Тесты для DIV_QQ_Q (деление)
    def test_div_qq_q(self):
        r1 = Rational("1", "2")
        r2 = Rational("1", "3")
        assert str(r1.div_qq_q(r2)) == "3/2"

        r3 = Rational("2", "3")
        r4 = Rational("4", "5")
        assert str(r3.div_qq_q(r4)) == "5/6"

        r5 = Rational("0", "5")
        r6 = Rational("10", "1")
        assert str(r5.div_qq_q(r6)) == "0/1"

        r7 = Rational("1", "2")
        r8 = Rational("-1", "3")
        assert str(r7.div_qq_q(r8)) == "-3/2"

        with pytest.raises(ZeroDivisionError):
            Rational("1", "2").div_qq_q(Rational("0", "5"))
