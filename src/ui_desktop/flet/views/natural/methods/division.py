import flet as ft
from natural.natural import Natural

def NaturalDivisionView():
    """Представление для неполного частного от деления (оператор //)"""
    num1_input = ft.TextField(label="Делимое (n1)", width=200)
    num2_input = ft.TextField(label="Делитель (n2, != 0)", width=200)
    result_text = ft.Text()

    def div_click(e):
        try:
            n1 = Natural(num1_input.value)
            n2 = Natural(num2_input.value)
            if n2.values == [0]:
                result_text.value = f"Ошибка: Деление на ноль."
                e.page.update()
                return
            result = n1 // n2 # Используем перегруженный оператор неполного частного
            result_text.value = f"Результат (n1 // n2): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    div_button = ft.ElevatedButton("Неполное частное (n1 // n2)", on_click=div_click)

    return ft.View(
        "/natural/division",
        [
            ft.AppBar(title=ft.Text("Неполное частное от деления"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Неполное частное от деления первого натурального на второе (делитель != 0)."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
                    div_button,
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
