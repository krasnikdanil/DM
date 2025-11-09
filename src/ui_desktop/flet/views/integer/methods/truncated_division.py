import flet as ft
from integer.integer import Integer

def IntegerTruncatedDivisionView():
    """Представление для деления двух целых чисел (округление к нулю)"""
    num1_input = ft.TextField(label="Делимое", width=200)
    num2_input = ft.TextField(label="Делитель", width=200)
    result_text = ft.Text()

    def div_click(e):
        try:
            n1 = Integer(num1_input.value)
            n2 = Integer(num2_input.value)
            if str(n2) == "0":
                raise ZeroDivisionError("Делитель не может быть равен нулю")
            result = n1 // n2 # Используем перегруженный оператор (__floordiv__)
            result_text.value = f"Частное: {result}"
        except (ValueError, TypeError, ZeroDivisionError) as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    div_button = ft.ElevatedButton("Разделить", on_click=div_click)

    return ft.View(
        "/integer/truncated_division",
        [
            ft.AppBar(title=ft.Text("Деление целых чисел (округление к нулю)"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Введите два целых числа для деления (второе не равно нулю)."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
                    div_button,
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
