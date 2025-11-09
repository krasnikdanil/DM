import flet as ft
from natural.natural import Natural

def NaturalLCMView():
    """Представление для вычисления НОК (lcm)"""
    num1_input = ft.TextField(label="Первое число (n1)", width=200)
    num2_input = ft.TextField(label="Второе число (n2)", width=200)
    result_text = ft.Text()

    def lcm_click(e):
        try:
            n1 = Natural(num1_input.value)
            n2 = Natural(num2_input.value)
            result = n1.lcm(n2) # Используем метод lcm из класса Natural
            result_text.value = f"НОК(n1, n2): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    lcm_button = ft.ElevatedButton("Вычислить НОК (n1, n2)", on_click=lcm_click)

    return ft.View(
        "/natural/lcm",
        [
            ft.AppBar(title=ft.Text("Наименьшее общее кратное"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Вычисление НОК двух натуральных чисел."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
                    lcm_button,
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
