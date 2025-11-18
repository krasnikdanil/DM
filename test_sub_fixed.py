import sys
import os

# Добавляем корневую папку проекта (где лежит 'src') в sys.path.
project_root = os.path.dirname(os.path.abspath(__file__)) # Это путь корню проекта
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

from rational.rational import Rational

print("Тестируем 12/15 - 3/3 после исправления")
r1 = Rational("12", "15")
r2 = Rational("3", "3")

print(f"r1 = {r1}")
print(f"r2 = {r2}")

result = r1.sub_qq_q(r2)
print(f"Результат r1.sub_qq_q(r2): {result}")
