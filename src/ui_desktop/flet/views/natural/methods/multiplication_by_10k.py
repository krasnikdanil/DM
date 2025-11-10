import flet as ft
from natural.natural import Natural

def NaturalMultiplicationBy10kView():
    """Представление для умножения натурального числа на 10^k (mul_10k)"""
    num_input = ft.TextField(label="Натуральное число", width=200)
    k_input = ft.TextField(label="Степень k (натуральное число)", width=100)
    result_text = ft.Text()

    def mul_click(e):
        try:
            n = Natural(num_input.value)
            k = int(k_input.value)
            if k < 0:
                 result_text.value = f"Ошибка: Степень k должна быть натуральным числом (>= 0)."
                 e.page.update()
                 return
            result = n.mul_10k(k) # Используем метод mul_10k из класса Natural, передаем k как int
            result_text.value = f"Результат (n * 10^{k}): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    mul_button = ft.ElevatedButton("Умножить (n * 10^k)", on_click=mul_click)

    return ft.View(
        "/natural/multiplication_by_10k",
        [
            ft.AppBar(title=ft.Text("Умножение натурального числа на 10^k"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Умножение натурального числа на 10 в степени k (k >= 0)."),
                    ft.Row([num_input, k_input], alignment=ft.MainAxisAlignment.CENTER),
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
