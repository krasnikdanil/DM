import flet as ft
from natural.natural import Natural

def NaturalMultiplicationView():
    """Представление для умножения двух натуральных чисел (оператор *)"""
    num1_input = ft.TextField(label="Первое число", width=200)
    num2_input = ft.TextField(label="Второе число", width=200)
    result_text = ft.Text()

    def mul_click(e):
        try:
            n1 = Natural(num1_input.value)
            n2 = Natural(num2_input.value)
            result = n1 * n2 # Используем перегруженный оператор умножения
            result_text.value = f"Результат (n1 * n2): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    mul_button = ft.ElevatedButton("Умножить (n1 * n2)", on_click=mul_click)

    return ft.View(
        "/natural/multiplication",
        [
            ft.AppBar(title=ft.Text("Умножение натуральных чисел"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Умножение двух натуральных чисел."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
                    mul_button,
                    result_text,
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/natural")),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )
