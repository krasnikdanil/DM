import flet as ft
from integer.integer import Integer

def IntegerMulByMinusOneView():
    """Представление для умножения целого числа на -1"""
    num_input = ft.TextField(label="Целое число", width=300)
    result_text = ft.Text()

    def mul_click(e):
        try:
            integer = Integer(num_input.value)
            result = -integer # Используем перегруженный унарный минус
            result_text.value = f"Результат: {result}"
        except (ValueError, TypeError) as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    mul_button = ft.ElevatedButton("Умножить на -1", on_click=mul_click)

    return ft.View(
        "/integer/mul_by_minus_one",
        [
            ft.AppBar(title=ft.Text("Умножение на -1"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Введите целое число для умножения на -1."),
                    num_input,
                    mul_button,
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
