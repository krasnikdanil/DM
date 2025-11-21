import flet as ft
from polynomial.polynomial import Polynomial
from rational.rational import Rational

class PolynomialSubPQView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/polynomial/sub_pq_p"
        self.appbar = ft.AppBar(title=ft.Text("Вычитание P(x)-Q"), bgcolor=ft.Colors.GREEN_700)
        
        self.poly_input = ft.TextField(label="Многочлен (например, 2*x^2 + x + 1)", width=400, value="0")
        self.rational_num_input = ft.TextField(label="Рациональное число (например, 1/2)", width=200, value="0/1")
        self.result_text = ft.Text(size=20)
        
        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [self.poly_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Text("-", size=24),
                    ft.Row(
                        [self.rational_num_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(text="Вычесть", on_click=self.subtract_rational_from_polynomial),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/polynomial")),
                    self.result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def subtract_rational_from_polynomial(self, e):
        try:
            poly = Polynomial.from_string(self.poly_input.value)
            # Парсим рациональное число
            rational_str = self.rational_num_input.value.strip()
            if '/' in rational_str:
                parts = rational_str.split('/')
                rational = Rational(parts[0].strip(), parts[1].strip())
            else:
                rational = Rational(rational_str, "1")
            
            result = poly.sub_pq_p(rational)
            
            self.result_text.value = f"Результат: {result}"
        except Exception as ex:
            self.result_text.value = f"Ошибка: {ex}"
        
        self.update()
