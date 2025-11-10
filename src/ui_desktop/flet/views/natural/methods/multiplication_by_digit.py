import flet as ft
from natural.natural import Natural

def NaturalMultiplicationByDigitView():
    """Представление для умножения натурального числа на цифру (mulnd)"""
    num_input = ft.TextField(label="Натуральное число", width=200)
    digit_input = ft.TextField(label="Цифра (0-9)", width=100)
    result_text = ft.Text()

    def mul_click(e):
        try:
            n = Natural(num_input.value)
            digit_str = digit_input.value
            if not (len(digit_str) == 1 and digit_str.isdigit()):
                result_text.value = f"Ошибка: Введите одиночную цифру (0-9)."
                e.page.update()
                return
            digit_natural = Natural(digit_str) # Создаем Natural из одной цифры
            result = n * digit_natural 
            result_text.value = f"Результат (n * digit): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    mul_button = ft.ElevatedButton("Умножить (n * digit)", on_click=mul_click)

    return ft.View(
        "/natural/multiplication_by_digit",
        [
            ft.AppBar(title=ft.Text("Умножение натурального числа на цифру"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Умножение натурального числа на цифру (0-9)."),
                    ft.Row([num_input, digit_input], alignment=ft.MainAxisAlignment.CENTER),
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
