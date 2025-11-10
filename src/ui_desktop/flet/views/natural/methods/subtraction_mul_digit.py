import flet as ft
from natural.natural import Natural

def NaturalSubtractionMulDigitView():
    """Представление для вычитания из натурального другого натурального, умноженного на цифру (sub_mul_digit)"""
    num1_input = ft.TextField(label="Первое число (n1)", width=200)
    num2_input = ft.TextField(label="Второе число (n2)", width=200)
    digit_input = ft.TextField(label="Цифра (0-9)", width=100)
    result_text = ft.Text()

    def sub_click(e):
        try:
            n1 = Natural(num1_input.value)
            n2 = Natural(num2_input.value)
            digit_str = digit_input.value
            if not (len(digit_str) == 1 and digit_str.isdigit()):
                result_text.value = f"Ошибка: Введите одиночную цифру (0-9)."
                e.page.update()
                return
            digit_int = int(digit_str)
            result = n1.sub_mul_digit(n2, digit_int) # Используем метод sub_mul_digit из класса Natural
            result_text.value = f"Результат (n1 - n2 * digit): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    sub_button = ft.ElevatedButton("Вычесть (n1 - n2 * digit)", on_click=sub_click)

    return ft.View(
        "/natural/subtraction_mul_digit",
        [
            ft.AppBar(title=ft.Text("Вычитание с умножением на цифру"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Вычитание из натурального другого натурального, умноженного на цифру (0-9)."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([digit_input], alignment=ft.MainAxisAlignment.CENTER), # Цифра отдельно
                    sub_button,
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
