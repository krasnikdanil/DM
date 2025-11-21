import flet as ft
from polynomial.polynomial import Polynomial

class PolynomialFacPQView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/polynomial/fac_p_q"
        self.appbar = ft.AppBar(title=ft.Text("Вынесение НОК/НОД"), bgcolor=ft.Colors.GREEN_700)
        
        self.poly_input = ft.TextField(label="Многочлен (например, 2/3*x^2 + 1/3*x)", width=400, value="0")
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.poly_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(text="Вынести НОК/НОД", on_click=self.factor_polynomial),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/polynomial")),
                    self.result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def factor_polynomial(self, e):
        try:
            poly = Polynomial.from_string(self.poly_input.value)
            
            result = poly.fac_p_q()
            
            self.result_text.value = f"Результат: {result}"
        except Exception as ex:
            self.result_text.value = f"Ошибка: {ex}"
        
        self.update()
