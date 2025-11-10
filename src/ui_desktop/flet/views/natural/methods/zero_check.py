import flet as ft
from natural.natural import Natural

def NaturalZeroCheckView():
    """Представление для метода nzernb (проверка на ноль)"""
    num_input = ft.TextField(label="Введите число", width=200)
    result_text = ft.Text()

    def check_click(e):
        try:
            n = Natural(num_input.value)
            result = n.nzernb() # Возвращает "Дa" или "Нет"
            result_text.value = f"{'Да' if result == 'Дa' else 'Нет'}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    check_button = ft.ElevatedButton("Проверить на ноль", on_click=check_click)

    return ft.View(
        "/natural/zero_check",
        [
            ft.AppBar(title=ft.Text("Проверка натурального числа на ноль"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Проверка: если число не равно нулю, то «да» иначе «нет»."),
                    num_input,
                    check_button,
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
