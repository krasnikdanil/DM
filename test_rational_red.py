from src.rational.rational import Rational

# Тестируем сокращение дроби с отрицательным числителем
r = Rational("-6", "9")
print(f"Исходная дробь: {r}")
reduced = r.red_q_q()
print(f"После сокращения: {reduced}")

r2 = Rational("6", "-9")
print(f"Исходная дробь: {r2}")
try:
    reduced2 = r2.red_q_q()
    print(f"После сокращения: {reduced2}")
except Exception as e:
    print(f"Ошибка при сокращении: {e}")

r3 = Rational("-6", "-9")
print(f"Исходная дробь: {r3}")
try:
    reduced3 = r3.red_q_q()
    print(f"После сокращения: {reduced3}")
except Exception as e:
    print(f"Ошибка при сокращении: {e}")
