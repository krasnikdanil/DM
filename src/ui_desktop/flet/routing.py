import flet as ft
from ui_desktop.flet.views import (
    IntegerView,
    RationalView,
    PolynomialView,
)

# Импортируем NaturalView отдельно
from ui_desktop.flet.views.natural_view import NaturalView
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
from ui_desktop.flet.views.natural.methods.gcd import NaturalGCDView
from ui_desktop.flet.views.natural.methods.division import NaturalDivisionView
from ui_desktop.flet.views.natural.methods.modulo import NaturalModuloView
from ui_desktop.flet.views.natural.methods.lcm import NaturalLCMView
from ui_desktop.flet.views.integer.methods.abs import IntegerAbsView
from ui_desktop.flet.views.integer.methods.sgn import IntegerSgnView
from ui_desktop.flet.views.integer.methods.mul_by_minus_one import IntegerMulByMinusOneView
from ui_desktop.flet.views.integer.methods.from_natural import IntegerFromNaturalView
from ui_desktop.flet.views.integer.methods.to_natural import IntegerToNaturalView
from ui_desktop.flet.views.integer.methods.addition import IntegerAdditionView
from ui_desktop.flet.views.integer.methods.subtraction import IntegerSubtractionView
from ui_desktop.flet.views.integer.methods.multiplication import IntegerMultiplicationView
from ui_desktop.flet.views.integer.methods.truncated_division import IntegerTruncatedDivisionView
from ui_desktop.flet.views.integer.methods.modulo import IntegerModuloView
from ui_desktop.flet.views.rational.methods.reduction import RationalReductionView
from ui_desktop.flet.views.rational.methods.addition import RationalAdditionView
from ui_desktop.flet.views.rational.methods.subtraction import RationalSubtractionView
from ui_desktop.flet.views.rational.methods.multiplication import RationalMultiplicationView
from ui_desktop.flet.views.rational.methods.division import RationalDivisionView
from ui_desktop.flet.views.rational.methods.is_integer import RationalIsIntegerView
from ui_desktop.flet.views.rational.methods.trans_z_q import RationalTransZQView
from ui_desktop.flet.views.rational.methods.trans_q_z import RationalTransQZView


# Словарь соответствия маршрутов и представлений
ROUTE_MAP = {
    "/natural": lambda: NaturalView(),
    "/natural/comparison": lambda: NaturalComparisonView(),
    "/natural/addition": lambda: NaturalAdditionView(),
    "/natural/zero_check": lambda: NaturalZeroCheckView(),
    "/natural/add_one": lambda: NaturalAddOneView(),
    "/natural/subtraction": lambda: NaturalSubtractionView(),
    "/natural/multiplication_by_digit": lambda: NaturalMultiplicationByDigitView(),
    "/natural/multiplication_by_10k": lambda: NaturalMultiplicationBy10kView(),
    "/natural/multiplication": lambda: NaturalMultiplicationView(),
    "/natural/subtraction_mul_digit": lambda: NaturalSubtractionMulDigitView(),
    "/natural/div_first_digit": lambda: NaturalDivFirstDigitView(),
    "/natural/lcm": lambda: NaturalLCMView(),
    "/natural/division": lambda: NaturalDivisionView(),
    "/natural/modulo": lambda: NaturalModuloView(),
    "/natural/gcd": lambda: NaturalGCDView(),
    "/integer": lambda: IntegerView(),
    "/rational": lambda: RationalView(),
    "/polynomial": lambda: PolynomialView(),
    "/integer/abs": lambda: IntegerAbsView(),
    "/integer/sgn": lambda: IntegerSgnView(),
    "/integer/mul_by_minus_one": lambda: IntegerMulByMinusOneView(),
    "/integer/from_natural": lambda: IntegerFromNaturalView(),
    "/integer/to_natural": lambda: IntegerToNaturalView(),
    "/integer/addition": lambda: IntegerAdditionView(),
    "/integer/subtraction": lambda: IntegerSubtractionView(),
    "/integer/multiplication": lambda: IntegerMultiplicationView(),
    "/integer/truncated_division": lambda: IntegerTruncatedDivisionView(),
    "/integer/modulo": lambda: IntegerModuloView(),
    "/rational/reduction": lambda: RationalReductionView(),
    "/rational/addition": lambda: RationalAdditionView(),
    "/rational/subtraction": lambda: RationalSubtractionView(),
    "/rational/multiplication": lambda: RationalMultiplicationView(),
    "/rational/division": lambda: RationalDivisionView(),
    "/rational/is_integer": lambda: RationalIsIntegerView(),
    "/rational/trans_z_q": lambda: RationalTransZQView(),
    "/rational/trans_q_z": lambda: RationalTransQZView(),
}

def handle_route_change(e: ft.RouteChangeEvent, page: ft.Page):
    """Обрабатывает изменение маршрута"""
    page.views.clear()
    page.views.append(
        ft.View(
            "/",
            [
                ft.AppBar(title=ft.Text("DMC"), actions=[get_theme_button(page)]),
                ft.Column(
                    [
                        ft.Text("Welcome to DMC", size=30),
                        ft.Row(
                            [
                                ft.ElevatedButton("Natural", on_click=lambda _: page.go("/natural")),
                                ft.ElevatedButton("Integer", on_click=lambda _: page.go("/integer")),
                                ft.ElevatedButton("Rational", on_click=lambda _: page.go("/rational")),
                                ft.ElevatedButton("Polynomial", on_click=lambda _: page.go("/polynomial")),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                )
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # Проверяем, есть ли маршрут в карте
    if e.route in ROUTE_MAP:
        view_constructor = ROUTE_MAP[e.route]
        page.views.append(view_constructor())

    page.update()


def get_theme_button(page: ft.Page) -> ft.IconButton:
    """Возвращает кнопку смены темы"""
    def change_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    return ft.IconButton(
        ft.Icons.WB_SUNNY_OUTLINED,
        on_click=change_theme,
        tooltip="Change theme"
    )


def handle_view_pop(e: ft.ViewPopEvent):
    """Обрабатывает возврат назад по стеку представлений"""
    e.page.views.pop()
    top_view = e.page.views[-1]
    e.page.go(top_view.route)
