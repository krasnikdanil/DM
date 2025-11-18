import flet as ft
from rational.rational import Rational

class RationalIsIntegerView(ft.View): # Inherit directly from ft.View
    def __init__(self):
        super().__init__()
        self.route = "/rational/is_integer" # Add route
        self.appbar = ft.AppBar(title=ft.Text("Проверка на целое"), bgcolor=ft.Colors.BROWN_700) # Add appbar
        
        self.num_input = ft.TextField(label="Числитель", width=200, value="0") # Direct TextField
        self.den_input = ft.TextField(label="Знаменатель", width=200, value="1") # Direct TextField
        self.result_text = ft.Text(size=20) # Direct Text for result

        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.num_input, ft.Text("/", size=30), self.den_input], # Combine into one row
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(
                        text="Проверка сокращенного дробного на целое",
                        icon=ft.Icons.CHECK,
                        on_click=self.check_is_integer,
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

    def check_is_integer(self, e):
        try:
            num_val = self.num_input.value
            den_val = self.den_input.value
            rational_num = Rational(num_val, den_val)
            
            is_integer = rational_num.int_q_b()

            if is_integer:
                self.result_text.value = "да"
            else:
                self.result_text.value = "нет"
            
            self.update()

        except Exception as ex:
            self.result_text.value = f"Ошибка: {ex}"
            self.update()
