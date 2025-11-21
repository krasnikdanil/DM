import flet as ft
from polynomial.polynomial import Polynomial
from natural.natural import Natural

class PolynomialMulPXKView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/polynomial/mul_pxk_p"
        self.appbar = ft.AppBar(title=ft.Text("Умножение P(x) на x^k"), bgcolor=ft.Colors.GREEN_700)
        
        self.poly_input = ft.TextField(label="Многочлен (например, 2*x^2 + x + 1)", width=400, value="0")
        self.k_input = ft.TextField(label="Степень k (натуральное или 0)", width=150, value="0")
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.poly_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Text("* x^", size=24),
                    ft.Row(
                        [self.k_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(text="Умножить", on_click=self.multiply_polynomial_by_xk),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/polynomial")),
                    self.result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def multiply_polynomial_by_xk(self, e):
        try:
            poly = Polynomial.from_string(self.poly_input.value)
            k_natural = Natural(self.k_input.value)
            
            result = poly.mul_pxk_p(k_natural)
            
            self.result_text.value = f"Результат: {result}"
        except Exception as ex:
            self.result_text.value = f"Ошибка: {ex}"
        
        self.update()
