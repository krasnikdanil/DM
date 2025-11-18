from src.rational.rational import Rational

# Тестируем вычитание дробей
print("Тест 1: 1/2 - 1/3")
r1 = Rational("1", "2")
r2 = Rational("1", "3")
result = r1.sub_qq_q(r2)
print(f"Результат: {result}")

print("\nТест 2: -1/2 - 1/3")
r1 = Rational("-1", "2")
r2 = Rational("1", "3")
result = r1.sub_qq_q(r2)
print(f"Результат: {result}")

print("\nТест 3: 1/2 - (-1)/3")
r1 = Rational("1", "2")
r2 = Rational("-1", "3")
result = r1.sub_qq_q(r2)
print(f"Результат: {result}")

print("\nТест 4: (-1)/2 - (-1)/3")
r1 = Rational("-1", "2")
r2 = Rational("-1", "3")
result = r1.sub_qq_q(r2)
print(f"Результат: {result}")
