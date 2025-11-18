from src.rational.rational import Rational

# Тестируем создание Rational с отрицательным числителем и положительным знаменателем
try:
    r = Rational("-12", "8")
    print(f"Rational('-12', '8') создан успешно: {r}")
    reduced = r.red_q_q()
    print(f"После сокращения: {reduced}")
except Exception as e:
    print(f"Ошибка при создании или сокращении Rational('-12', '8'): {e}")

# Тестируем создание Integer и Natural отдельно
try:
    from src.integer.integer import Integer
    from src.natural.natural import Natural

    i = Integer("-12")
    print(f"Integer('-12') создан успешно: {i}")

    n = Natural("8")
    print(f"Natural('8') создан успешно: {n}")
except Exception as e:
    print(f"Ошибка при создании Integer или Natural: {e}")
