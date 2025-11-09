import flet as ft
from integer.integer import Integer

def IntegerModuloView():
    """Представление для нахождения остатка от деления двух целых чисел"""
    num1_input = ft.TextField(label="Делимое", width=200)
    num2_input = ft.TextField(label="Делитель", width=200)
    result_text = ft.Text()

    def mod_click(e):
        try:
            n1 = Integer(num1_input.value)
            n2 = Integer(num2_input.value)
            if str(n2) == "0":
                raise ZeroDivisionError("Делитель не может быть равен нулю")
            result = n1 % n2 # Используем перегруженный оператор (__mod__)
            result_text.value = f"Остаток: {result}"
        except (ValueError, TypeError, ZeroDivisionError) as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    mod_button = ft.ElevatedButton("Найти остаток", on_click=mod_click)

    return ft.View(
        "/integer/modulo",
        [
            ft.AppBar(title=ft.Text("Остаток от деления целых чисел"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Введите два целых числа для деления (делитель не равен нулю)."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
                    mod_button,
                    result_text,
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/integer")),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )
