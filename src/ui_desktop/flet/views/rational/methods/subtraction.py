import flet as ft
from rational.rational import Rational

class RationalSubtractionView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/rational/subtraction"
        self.appbar = ft.AppBar(title=ft.Text("Вычитание дробей"), bgcolor=ft.Colors.BROWN_700)
        
        self.num1_input = ft.TextField(label="Числитель 1", width=150)
        self.den1_input = ft.TextField(label="Знаменатель 1", value="1", width=150)
        self.num2_input = ft.TextField(label="Числитель 2", width=150)
        self.den2_input = ft.TextField(label="Знаменатель 2", value="1", width=150)
        
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.num1_input, self.den1_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Text("-", size=24),
                    ft.Row(
                        [self.num2_input, self.den2_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(text="Вычесть", on_click=self.subtract_fractions),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/rational")),
                    self.result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def subtract_fractions(self, e):
        try:
            r1 = Rational(self.num1_input.value, self.den1_input.value)
            r2 = Rational(self.num2_input.value, self.den2_input.value)
            
            result = r1 - r2
            
            self.result_text.value = f"Результат: {result}"
        except (ValueError, ZeroDivisionError) as err:
            self.result_text.value = f"Ошибка: {err}"
        
        self.update()
