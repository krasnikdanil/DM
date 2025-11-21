import flet as ft
from ui_desktop.flet.views.natural.methods.comparison import NaturalComparisonView
from ui_desktop.flet.views.natural.methods.addition import NaturalAdditionView
from ui_desktop.flet.views.natural.methods.zero_check import NaturalZeroCheckView
from ui_desktop.flet.views.natural.methods.add_one import NaturalAddOneView
from ui_desktop.flet.views.natural.methods.subtraction import NaturalSubtractionView
from ui_desktop.flet.views.natural.methods.multiplication_by_digit import NaturalMultiplicationByDigitView
from ui_desktop.flet.views.natural.methods.multiplication_by_10k import NaturalMultiplicationBy10kView
from ui_desktop.flet.views.natural.methods.multiplication import NaturalMultiplicationView
from ui_desktop.flet.views.natural.methods.subtraction_mul_digit import NaturalSubtractionMulDigitView
from ui_desktop.flet.views.natural.methods.div_first_digit import NaturalDivFirstDigitView
from ui_desktop.flet.views.natural.methods.lcm import NaturalLCMView
from ui_desktop.flet.views.natural.methods.gcd import NaturalGCDView
from ui_desktop.flet.views.natural.methods.division import NaturalDivisionView
from ui_desktop.flet.views.natural.methods.modulo import NaturalModuloView

class NaturalView(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/natural"
        self.appbar = ft.AppBar(title=ft.Text("Натуральные числа"), bgcolor=ft.Colors.BROWN_400)
        self.controls = [
            ft.Column(
                [
                    ft.Text("Выберите метод:", size=20),
                    ft.GridView(
                        controls=[
                            self.create_button("Сравнение (COM_NN_D)", "/natural/comparison"),
                            self.create_button("Сложение (ADD_NN_N)", "/natural/addition"),
                            self.create_button("Проверка на ноль (NZER_N_B)", "/natural/zero_check"),
                            self.create_button("Добавить 1(ADD_1N_N)", "/natural/add_one"),
                            self.create_button("Вычитание (SUB_NN_N)", "/natural/subtraction"),
                            self.create_button("Умножение на цифру (MUL_ND_N)", "/natural/multiplication_by_digit"),
                            self.create_button("Умножение на 10^k (MUL_Nk_N)", "/natural/multiplication_by_10k"),
                            self.create_button("Умножение (MUL_NN_N)", "/natural/multiplication"),
                            self.create_button("Вычитание с умножением на цифру (SUB_NDN_N)", "/natural/subtraction_mul_digit"),
                            self.create_button("Первая цифра деления * 10^k (DIV_NN_Dk)", "/natural/div_first_digit"),
                            self.create_button("НОК (LCM_NN_N)", "/natural/lcm"),
                            self.create_button("НОД (GCD_NN_N)", "/natural/gcd"),
                            self.create_button("Неполное частное (DIV_NN_N)", "/natural/division"),
                            self.create_button("Остаток от деления (MOD_NN_N)", "/natural/modulo"),
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
