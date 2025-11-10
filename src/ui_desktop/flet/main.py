import sys
import os
import flet as ft

# Добавляем корень проекта (папку 'src') в sys.path
# Это позволяет использовать абсолютные импорты от 'src'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

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

def main(page: ft.Page):
    page.title = "DMC Flet"
    page.theme_mode = ft.ThemeMode.DARK

    def change_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    theme_button = ft.IconButton(
        ft.Icons.WB_SUNNY_OUTLINED,
        on_click=change_theme,
        tooltip="Change theme"
    )

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("DMC"), actions=[theme_button]),
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
        if e.route == "/natural":
            page.views.append(NaturalView())
        elif e.route == "/natural/comparison":
            page.views.append(NaturalComparisonView())
        elif e.route == "/natural/addition":
            page.views.append(NaturalAdditionView())
        elif e.route == "/natural/zero_check":
            page.views.append(NaturalZeroCheckView())
        elif e.route == "/natural/add_one":
            page.views.append(NaturalAddOneView())
        elif e.route == "/natural/subtraction":
            page.views.append(NaturalSubtractionView())
        elif e.route == "/natural/multiplication_by_digit":
            page.views.append(NaturalMultiplicationByDigitView())
        elif e.route == "/natural/multiplication_by_10k":
            page.views.append(NaturalMultiplicationBy10kView())
        elif e.route == "/natural/multiplication":
            page.views.append(NaturalMultiplicationView())
        elif e.route == "/natural/subtraction_mul_digit":
            page.views.append(NaturalSubtractionMulDigitView())
        elif e.route == "/natural/div_first_digit":
            page.views.append(NaturalDivFirstDigitView())
        elif e.route == "/natural/lcm":
            page.views.append(NaturalLCMView())
        elif e.route == "/natural/division":
            page.views.append(NaturalDivisionView())
        elif e.route == "/natural/modulo":
            page.views.append(NaturalModuloView())
        elif e.route == "/natural/gcd":
            page.views.append(NaturalGCDView())
        elif e.route == "/integer":
            page.views.append(IntegerView())
        elif e.route == "/rational":
            page.views.append(RationalView())
        elif e.route == "/polynomial":
            page.views.append(PolynomialView())
        elif e.route == "/integer/abs":
            page.views.append(IntegerAbsView())
        elif e.route == "/integer/sgn":
            page.views.append(IntegerSgnView())
        elif e.route == "/integer/mul_by_minus_one":
            page.views.append(IntegerMulByMinusOneView())
        elif e.route == "/integer/from_natural":
            page.views.append(IntegerFromNaturalView())
        elif e.route == "/integer/to_natural":
            page.views.append(IntegerToNaturalView())
        elif e.route == "/integer/addition":
            page.views.append(IntegerAdditionView())
        elif e.route == "/integer/subtraction":
            page.views.append(IntegerSubtractionView())
        elif e.route == "/integer/multiplication":
            page.views.append(IntegerMultiplicationView())
        elif e.route == "/integer/truncated_division":
            page.views.append(IntegerTruncatedDivisionView())
        elif e.route == "/integer/modulo":
            page.views.append(IntegerModuloView())
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
