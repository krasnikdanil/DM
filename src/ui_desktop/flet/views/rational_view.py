import flet as ft

class RationalView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/rational"
        self.appbar = ft.AppBar(title=ft.Text("Рациональные числа"), bgcolor=ft.Colors.BROWN_400)
        self.controls = [
            ft.Column(
                [
                    ft.Text("Выберите метод:", size=20),
                    ft.GridView(
                        controls=[
                            self.create_button("Сокращение (RED_Q_Q)", "/rational/reduction"),
                            self.create_button("Сложение (ADD_QQ_Q)", "/rational/addition"),
                            self.create_button("Вычитание (SUB_QQ_Q)", "/rational/subtraction"),
                            self.create_button("Умножение (MUL_QQ_Q)", "/rational/multiplication"),
                            self.create_button("Деление (DIV_QQ_Q)", "/rational/division"),
                            self.create_button("Проверка на целое", "/rational/is_integer"),
                            self.create_button("Целое в дробное (TRANS_Z_Q)", "/rational/trans_z_q"),
                            self.create_button("Дробное в целое (TRANS_Q_Z)", "/rational/trans_q_z"),
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
