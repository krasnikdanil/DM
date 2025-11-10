import flet as ft
from integer.integer import Integer

def IntegerSgnView():
    """Представление для определения знака целого числа (SGN_Z_D)"""
    num_input = ft.TextField(label="Целое число", width=300)
    result_text = ft.Text()

    def sgn_click(e):
        try:
            integer = Integer(num_input.value)
            result = integer.poz()
            result_text.value = f"Результат (SGN_Z_D): {result}"
        except (ValueError, TypeError) as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    sgn_button = ft.ElevatedButton("Определить знак", on_click=sgn_click)

    return ft.View(
        "/integer/sgn",
        [
            ft.AppBar(title=ft.Text("Определение знака (SGN_Z_D)"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Введите целое число для определения его знака."),
                    num_input,
                    sgn_button,
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
