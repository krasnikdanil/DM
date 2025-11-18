import flet as ft
from rational.rational import Rational

class RationalReductionView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/rational/reduction"
        self.appbar = ft.AppBar(title=ft.Text("Сокращение дроби"), bgcolor=ft.Colors.BROWN_700)
        
        self.num_input = ft.TextField(label="Числитель", width=200)
        self.den_input = ft.TextField(label="Знаменатель", width=200, value="1")
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.num_input, self.den_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(text="Сократить", on_click=self.reduce_fraction),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/rational")),
                    self.result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def reduce_fraction(self, e):
        try:
            num_str = self.num_input.value
            den_str = self.den_input.value

            if not num_str or not den_str:
                self.result_text.value = "Ошибка: Введите числитель и знаменатель"
                self.update()
                return

            original_fraction = Rational(num_str, den_str)
            reduced_fraction = original_fraction.red_q_q()
            
            self.result_text.value = f"Результат: {reduced_fraction}"
        except (ValueError, ZeroDivisionError) as err:
            self.result_text.value = f"Ошибка: {err}"
        
        self.update()
