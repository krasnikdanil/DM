import flet as ft
from integer.integer import Integer

def IntegerAbsView():
    """Представление для вычисления абсолютного значения (модуля) целого числа."""
    num_input = ft.TextField(label="Целое число", width=300)
    result_text = ft.Text()

    def abs_click(e):
        try:
            integer_num = Integer(num_input.value)
            # Используем __abs__(), который вызывается встроенной функцией abs()
            result = abs(integer_num)
            result_text.value = f"Абсолютное значение: {result} (тип: {type(result).__name__})"
        except (ValueError, TypeError) as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    abs_button = ft.ElevatedButton("Вычислить абсолютное значение", on_click=abs_click)

    return ft.View(
        "/integer/abs",
        [
            ft.AppBar(title=ft.Text("Абсолютная величина числа"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Вычисление абсолютного значения (модуля) целого числа. Результатом является натуральное число."),
                    num_input,
                    abs_button,
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
