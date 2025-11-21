import flet as ft
from ui_desktop.flet.views.integer.methods.abs import IntegerAbsView

class IntegerView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/integer"
        self.appbar = ft.AppBar(title=ft.Text("Целые числа"), bgcolor=ft.Colors.BROWN_400)
        self.controls = [
            ft.Column(
                [
                    ft.Text("Выберите метод:", size=20),
                    ft.GridView(
                        controls=[
                            self.create_button("Абсолютная величина (ABS_Z_N)", "/integer/abs"),
                            self.create_button("Определение знака (SGN_Z_D)", "/integer/sgn"),
                            self.create_button("Умножение на -1(MUL_ZM_Z)", "/integer/mul_by_minus_one"),
                            self.create_button("Из натурального в целое (TRANS_N_Z)", "/integer/from_natural"),
                            self.create_button("В натуральное (TRANS_Z_N)", "/integer/to_natural"),
                            self.create_button("Сложение (ADD_ZZ_Z)", "/integer/addition"),
                            self.create_button("Вычитание (SUB_ZZ_Z)", "/integer/subtraction"),
                            self.create_button("Умножение (MUL_ZZ_Z)", "/integer/multiplication"),
                            self.create_button("Частное (DIV_ZZ_Z)", "/integer/truncated_division"),
                            self.create_button("Остаток (MOD_ZZ_Z)", "/integer/modulo"),
                        ],
                        run_spacing=5,
                        spacing=5,
                        expand=True,
                        max_extent=160,
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
            width=150,
            height=70,
            bgcolor=ft.Colors.BROWN_300,
            border_radius=5,
            padding=5,
            ink=True,
            on_click=lambda e: e.page.go(route),
        )
