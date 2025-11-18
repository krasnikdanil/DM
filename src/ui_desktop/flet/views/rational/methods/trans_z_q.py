import flet as ft
from rational.rational import Rational
from integer.integer import Integer # Import Integer

class RationalTransZQView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/rational/trans_z_q"
        self.appbar = ft.AppBar(title=ft.Text("Преобразование целого в дробное"), bgcolor=ft.Colors.BROWN_700)
        
        self.integer_input = ft.TextField(label="Целое число", width=200, value="0")
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.integer_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(
                        text="Преобразовать в дробное",
                        icon=ft.Icons.TRANSFORM, # Using a generic transform icon
                        on_click=self.transform_integer_to_rational,
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

    def transform_integer_to_rational(self, e):
        try:
            integer_str = self.integer_input.value

            if not integer_str:
                self.result_text.value = "Ошибка: Введите целое число"
                self.update()
                return

            # Use the Integer class for input
            int_num = Integer(integer_str)
            rational_num = Rational.trans_z_q(int_num)
            
            self.result_text.value = f"Результат: {rational_num}"
        except Exception as ex:
            self.result_text.value = f"Ошибка: {ex}"
        
        self.update()
