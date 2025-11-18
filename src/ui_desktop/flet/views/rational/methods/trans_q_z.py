import flet as ft
from rational.rational import Rational
from integer.integer import Integer # Import Integer

class RationalTransQZView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/rational/trans_q_z"
        self.appbar = ft.AppBar(title=ft.Text("Дробное в целое"), bgcolor=ft.Colors.BROWN_700)
        
        self.num_input = ft.TextField(label="Числитель", width=200, value="0")
        self.den_input = ft.TextField(label="Знаменатель", width=200, value="1")
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.num_input, ft.Text("/", size=30), self.den_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(
                        text="Преобразовать в целое",
                        icon=ft.Icons.TRANSFORM,
                        on_click=self.transform_rational_to_integer,
                    ),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/rational")),
                    self.result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def transform_rational_to_integer(self, e):
        try:
            num_str = self.num_input.value
            den_str = self.den_input.value

            if not num_str or not den_str:
                self.result_text.value = "Ошибка: Введите числитель и знаменатель"
                self.update()
                return

            rational_num = Rational(num_str, den_str)
            integer_num = rational_num.trans_q_z() # Call trans_q_z()
            
            self.result_text.value = f"Результат: {integer_num}"
        except Exception as ex:
            self.result_text.value = f"Ошибка: {ex}"
        
        self.update()
