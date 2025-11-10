import flet as ft
from natural.natural import Natural

def NaturalAddOneView():
    """Представление для добавления 1 к натуральному числу"""
    num_input = ft.TextField(label="Введите число", width=200)
    result_text = ft.Text()

    def add_one_click(e):
        try:
            n = Natural(num_input.value)
            one = Natural("1")
            result = n + one # Используем перегруженный оператор сложения
            result_text.value = f"Результат (n + 1): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    add_button = ft.ElevatedButton("Добавить 1", on_click=add_one_click)

    return ft.View(
        "/natural/add_one",
        [
            ft.AppBar(title=ft.Text("Добавление 1 к натуральному числу"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Введите натуральное число. К нему будет добавлена 1."),
                    num_input,
                    add_button,
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
