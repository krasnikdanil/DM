import flet as ft
from integer.integer import Integer
from natural.natural import Natural

def IntegerToNaturalView():
    """Представление для преобразования целого неотрицательного числа в натуральное"""
    num_input = ft.TextField(label="Целое неотрицательное число", width=300)
    result_text = ft.Text()

    def convert_click(e):
        try:
            integer_num = Integer(num_input.value)
            result = integer_num.to_natural()
            result_text.value = f"Результат: {result}"
        except (ValueError, TypeError) as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    convert_button = ft.ElevatedButton("Преобразовать", on_click=convert_click)

    return ft.View(
        "/integer/to_natural",
        [
            ft.AppBar(title=ft.Text("Преобразование из целого в натуральное"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Введите целое неотрицательное число для преобразования в натуральное."),
                    num_input,
                    convert_button,
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
