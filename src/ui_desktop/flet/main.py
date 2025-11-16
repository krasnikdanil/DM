import sys
import os
import flet as ft

# Добавляем корень проекта (папку 'src') в sys.path
# Это позволяет использовать абсолютные импорты от 'src'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from ui_desktop.flet.routing import handle_route_change, handle_view_pop, get_theme_button

def main(page: ft.Page):
    page.title = "DMC"
    page.theme_mode = ft.ThemeMode.DARK

    theme_button = get_theme_button(page)

    def route_change_wrapper(e: ft.RouteChangeEvent):
        handle_route_change(e, page)

    page.on_route_change = route_change_wrapper
    page.on_view_pop = handle_view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
