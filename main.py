import sys
import os
import flet as ft

# Добавляем корневую папку проекта (где лежит 'src') в sys.path.
# Это позволяет Python находить пакет 'src' и все его подпакеты.
# sys.path.insert(0, ...) добавляет путь в начало списка, что имеет приоритет.
project_root = os.path.dirname(os.path.abspath(__file__)) # Это путь корню проекта
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

# Теперь, когда 'src' находится в пути, мы можем импортировать
# модуль изнутри 'src' используя абсолютный путь от 'src'.
from ui_desktop.flet.main import main as flet_main

if __name__ == "__main__":
    # Запускаем Fletы приложение.
    # Функция flet_main из 'src/ui_desktop/flet/main.py' теперь может
    # использовать относительные импорты, так как 'src' находится в sys.path.
    ft.app(target=flet_main)
