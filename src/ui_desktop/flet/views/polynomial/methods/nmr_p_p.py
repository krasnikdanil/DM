import flet as ft
from polynomial.polynomial import Polynomial

class PolynomialNmrPPView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/polynomial/nmr_p_p"
        self.appbar = ft.AppBar(title=ft.Text("Кратные корни в простые"), bgcolor=ft.Colors.GREEN_700)
        
        self.poly_input = ft.TextField(label="Многочлен (например, x^3 - 3*x^2 + 3*x - 1)", width=400, value="0")
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.poly_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(text="Преобразовать", on_click=self.transform_polynomial_roots),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/polynomial")),
                    self.result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def transform_polynomial_roots(self, e):
        try:
            poly = Polynomial.from_string(self.poly_input.value)
            
            result = poly.nmr_p_p()
            
            self.result_text.value = f"Результат: {result}"
        except Exception as ex:
            self.result_text.value = f"Ошибка: {ex}"
        
        self.update()
