import flet as ft
from natural.natural import Natural

def NaturalSubtractionView():
    """Представление для вычитания из первого большего натурального числа второго меньшего или равного (subnn)"""
    num1_input = ft.TextField(label="Большее число (n1)", width=200)
    num2_input = ft.TextField(label="Меньшее или равное число (n2)", width=200)
    result_text = ft.Text()

    def sub_click(e):
        try:
            n1 = Natural(num1_input.value)
            n2 = Natural(num2_input.value)
            # Проверим, действительно ли n1 >= n2, как того требует метод subnn
            if n1 < n2:
                 result_text.value = f"Ошибка: Первое число должно быть больше или равно второму."
            else:
                result = n1.subnn(n2) # Используем метод subnn из класса Natural
                result_text.value = f"Результат (n1 - n2): {result}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    sub_button = ft.ElevatedButton("Вычесть (n1 - n2)", on_click=sub_click)

    return ft.View(
        "/natural/subtraction",
        [
            ft.AppBar(title=ft.Text("Вычитание натуральных чисел (n1 >= n2)"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Вычитание из первого большего натурального числа второго меньшего или равного."),
                    ft.Row([num1_input, num2_input], alignment=ft.MainAxisAlignment.CENTER),
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
