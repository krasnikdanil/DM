import flet as ft
from natural.natural import Natural

def NaturalGCDView():
    """Представление для вычисления НОД (gcd)"""
    num1_input = ft.TextField(label="Первое число (n1)", width=200)
    num2_input = ft.TextField(label="Второе число (n2)", width=200)
    result_text = ft.Text()

    def gcd_click(e):
        try:
            n1 = Natural(num1_input.value)
            n2 = Natural(num2_input.value)
            result = n1.gcd(n2) # Используем метод gcd из класса Natural
            result_text.value = f"НОД(n1, n2): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    gcd_button = ft.ElevatedButton("Вычислить НОД (n1, n2)", on_click=gcd_click)

    return ft.View(
        "/natural/gcd",
        [
            ft.AppBar(title=ft.Text("Наибольший общий делитель"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Вычисление НОД двух натуральных чисел."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
                    gcd_button,
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
