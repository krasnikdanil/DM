import flet as ft
from natural.natural import Natural

def NaturalDivFirstDigitView():
    """Представление для вычисления первой цифры деления (div_first_digit)"""
    num1_input = ft.TextField(label="Большее число (n1)", width=200)
    num2_input = ft.TextField(label="Меньшее число (n2)", width=200)
    result_text = ft.Text()

    def div_click(e):
        try:
            n1 = Natural(num1_input.value)
            n2 = Natural(num2_input.value)
            if n2.values == [0]:
                result_text.value = f"Ошибка: Деление на ноль."
                e.page.update()
                return
            # Проверим, что n1 >= n2, как того требует метод в комментарии к div_first_digit
            if n1 < n2:
                 result_text.value = f"Ошибка: Первое число должно быть больше или равно второму."
                 e.page.update()
                 return
            digit, k = n1.div_first_digit(n2) # Используем метод div_first_digit из класса Natural, возвращает кортеж
            result = Natural(str(digit)).mul_10k(k) # Умножаем цифру на 10^k
            result_text.value = f"Результат (digit * 10^k): {result}. Первая цифра: {digit}, позиция k: {k}"
        except ValueError as err:
            result_text.value = f"Ошибка: {err}"
        e.page.update()

    div_button = ft.ElevatedButton("Вычислить (digit * 10^k)", on_click=div_click)

    return ft.View(
        "/natural/div_first_digit",
        [
            ft.AppBar(title=ft.Text("Первая цифра деления * 10^k"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Вычисление первой цифры деления большего на меньшее, домноженное на 10^k."),
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
