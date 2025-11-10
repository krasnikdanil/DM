import flet as ft
from natural.natural import Natural

def NaturalComparisonView():
    """Представление для метода comnn (сравнение)"""
    num1_input = ft.TextField(label="Первое число", width=200)
    num2_input = ft.TextField(label="Второе число", width=200)
    result_text = ft.Text()

    def compare_click(e):
        try:
            n1 = Natural(num1_input.value)
            n2 = Natural(num2_input.value)
            result = n1.comnn(n2)
            result_text.value = f"Результат: {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    compare_button = ft.ElevatedButton("Сравнить", on_click=compare_click)

    return ft.View(
        "/natural/comparison",
        [
            ft.AppBar(title=ft.Text("Сравнение натуральных чисел"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Сравнение: 2 - если первое больше второго, 0, если равно, 1 иначе."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
                    compare_button,
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
