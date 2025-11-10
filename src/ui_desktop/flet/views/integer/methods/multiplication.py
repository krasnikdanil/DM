import flet as ft
from integer.integer import Integer

def IntegerMultiplicationView():
    """Представление для умножения двух целых чисел"""
    num1_input = ft.TextField(label="Первое число", width=200)
    num2_input = ft.TextField(label="Второе число", width=200)
    result_text = ft.Text()

    def mul_click(e):
        try:
            n1 = Integer(num1_input.value)
            n2 = Integer(num2_input.value)
            result = n1 * n2 # Используем перегруженный оператор
            result_text.value = f"Результат: {result}"
        except (ValueError, TypeError) as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    mul_button = ft.ElevatedButton("Умножить", on_click=mul_click)

    return ft.View(
        "/integer/multiplication",
        [
            ft.AppBar(title=ft.Text("Умножение целых чисел"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Введите два целых числа для умножения."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
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
