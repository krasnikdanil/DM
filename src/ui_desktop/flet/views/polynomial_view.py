import flet as ft

class PolynomialView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/polynomial"
        self.appbar = ft.AppBar(title=ft.Text("Многочлены"), bgcolor=ft.Colors.BROWN_400)
        self.controls = [
            ft.Column(
                [
                    ft.Text("Выберите метод:", size=20),
                    ft.GridView(
                        controls=[
                            self.create_button("Сложение P(x)+P(x)", "/polynomial/add_pp_p"),
                            self.create_button("Сложение P(x)+Q", "/polynomial/add_pq_p"),
                            self.create_button("Вычитание P(x)-P(x)", "/polynomial/sub_pp_p"),
                            self.create_button("Вычитание P(x)-Q", "/polynomial/sub_pq_p"),
                            self.create_button("Умножение P(x)*Q", "/polynomial/mul_pq_p"),
                            self.create_button("Умножение P(x)*x^k", "/polynomial/mul_pxk_p"),
                            self.create_button("Старший коэффициент", "/polynomial/led_p_q"),
                            self.create_button("Степень многочлена", "/polynomial/deg_p_n"),
                            self.create_button("Вынесение НОК/НОД", "/polynomial/fac_p_q"),
                            self.create_button("Умножение P(x)*P(x)", "/polynomial/mul_pp_p"),
                            self.create_button("Деление P(x)/P(x)", "/polynomial/div_pp_p"),
                            self.create_button("Остаток P(x)%P(x)", "/polynomial/mod_pp_p"),
                            self.create_button("НОД многочленов", "/polynomial/gcf_pp_p"),
                            self.create_button("Производная многочлена", "/polynomial/der_p_p"),
                            self.create_button("Кратные корни в простые", "/polynomial/nmr_p_p"),
                        ],
                        run_spacing=10,
                        spacing=10,
                        expand=True,
                        max_extent=200,
                    ),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/")),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        ]
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def create_button(self, text, route):
        return ft.Container(
            content=ft.Text(text, text_align=ft.TextAlign.CENTER),
            width=180,
            height=80,
            bgcolor=ft.Colors.BROWN_300,
            border_radius=5,
            padding=10,
            ink=True,
            on_click=lambda e: e.page.go(route),
        )
