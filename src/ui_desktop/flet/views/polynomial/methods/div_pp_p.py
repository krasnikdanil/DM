import flet as ft
from polynomial.polynomial import Polynomial

class PolynomialDivPPView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/polynomial/div_pp_p"
        self.appbar = ft.AppBar(title=ft.Text("Частное от деления P(x)/P(x)"), bgcolor=ft.Colors.GREEN_700)
        
        self.poly1_input = ft.TextField(label="Делимое (P1(x))", width=400, value="0")
        self.poly2_input = ft.TextField(label="Делитель (P2(x))", width=400, value="1")
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.poly1_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Text("/", size=24),
                    ft.Row(
                        [self.poly2_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(text="Разделить", on_click=self.divide_polynomials),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/polynomial")),
                    self.result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def divide_polynomials(self, e):
        try:
            poly1 = Polynomial.from_string(self.poly1_input.value)
            poly2 = Polynomial.from_string(self.poly2_input.value)
            
            result = poly1.div_pp_p(poly2)
            
            self.result_text.value = f"Результат: {result}"
        except Exception as ex:
            self.result_text.value = f"Ошибка: {ex}"
        
        self.update()
