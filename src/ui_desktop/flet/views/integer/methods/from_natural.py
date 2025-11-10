import flet as ft
from integer.integer import Integer
from natural.natural import Natural

def IntegerFromNaturalView():
    """Представление для преобразования натурального числа в целое"""
    num_input = ft.TextField(label="Натуральное число", width=300)
    result_text = ft.Text()

    def convert_click(e):
        try:
            natural_num = Natural(num_input.value)
            result = Integer.from_natural(natural_num)
            result_text.value = f"Результат: {result}"
        except (ValueError, TypeError) as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    convert_button = ft.ElevatedButton("Преобразовать", on_click=convert_click)

    return ft.View(
        "/integer/from_natural",
        [
            ft.AppBar(title=ft.Text("Преобразование из натурального в целое"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Введите натуральное число для преобразования в целое."),
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
