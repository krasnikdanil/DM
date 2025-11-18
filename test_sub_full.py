from src.rational.rational import Rational

print("Тестируем 12/15 - 3/3")
r1 = Rational("12", "15")
r2 = Rational("3", "3")

print(f"r1 = {r1}")
print(f"r2 = {r2}")

result = r1.sub_qq_q(r2)
print(f"Результат r1.sub_qq_q(r2): {result}")

# Проверим внутренние значения
common_den = r1.den.lcm(r2.den)
print(f"Общий знаменатель (lcm): {common_den}")

k1 = common_den // r1.den
k2 = common_den // r2.den
print(f"k1 (множитель для r1): {k1}")
print(f"k2 (множитель для r2): {k2}")

num1_scaled = r1.num * Rational(str(k1)).num # Это Integer("1") * Integer("12")
num2_scaled = r2.num * Rational(str(k2)).num # Это Integer("5") * Integer("3")
print(f"Числитель r1 * k1: {num1_scaled}")
print(f"Числитель r2 * k2: {num2_scaled}")

new_num = num1_scaled - num2_scaled
print(f"Новый числитель (после вычитания): {new_num}")

# Проверим результат до сокращения
temp_result = Rational(str(new_num), str(common_den))
print(f"Временный результат до сокращения: {temp_result}")

final_result = temp_result.red_q_q()
print(f"Финальный результат после сокращения: {final_result}")
