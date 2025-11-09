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

def NaturalView():
    """Основное представление для натуральных чисел с выбором метода"""
    return ft.View(
        "/natural",
        [
            ft.AppBar(title=ft.Text("Натуральные числа"), bgcolor=ft.Colors.BROWN_400),
            ft.Column(
                [
                    ft.Text("Выберите метод:", size=20),
                    ft.GridView(
                        controls=[
                            ft.Container(
                                content=ft.Text("Сравнение (COM_NN_D)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True, # Включает эффект нажатия
                                on_click=lambda e: e.page.go("/natural/comparison"),
                            ),
                            ft.Container(
                                content=ft.Text("Сложение (ADD_NN_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/addition"),
                            ),
                            ft.Container(
                                content=ft.Text("Проверка на ноль (NZER_N_B)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/zero_check"),
                            ),
                            ft.Container(
                                content=ft.Text("Добавить 1(ADD_1N_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/add_one"),
                            ),
                            ft.Container(
                                content=ft.Text("Вычитание (SUB_NN_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/subtraction"),
                            ),
                            ft.Container(
                                content=ft.Text("Умножение на цифру (MUL_ND_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/multiplication_by_digit"),
                            ),
                            ft.Container(
                                content=ft.Text("Умножение на 10^k (MUL_Nk_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/multiplication_by_10k"),
                            ),
                            ft.Container(
                                content=ft.Text("Умножение (MUL_NN_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/multiplication"),
                            ),
                            ft.Container(
                                content=ft.Text("Вычитание с умножением на цифру (SUB_NDN_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/subtraction_mul_digit"),
                            ),
                            ft.Container(
                                content=ft.Text("Первая цифра деления * 10^k (DIV_NN_Dk)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/div_first_digit"),
                            ),
                            ft.Container(
                                content=ft.Text("НОК (LCM_NN_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/lcm"),
                            ),
                            ft.Container(
                                content=ft.Text("НОД (GCD_NN_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/gcd"),
                            ),
                            # Здесь можно добавить Container для других методов
                            ft.Container(
                                content=ft.Text("Неполное частное (DIV_NN_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/division"),
                            ),
                            ft.Container(
                                content=ft.Text("Остаток от деления (MOD_NN_N)", text_align=ft.TextAlign.CENTER),
                                width=150,
                                height=70,
                                bgcolor=ft.Colors.BROWN_200,
                                border_radius=5,
                                padding=5,
                                ink=True,
                                on_click=lambda e: e.page.go("/natural/modulo"),
                            ),
                        ],
                        run_spacing=5, # Уменьшено расстояние между строками/колонками
                        spacing=5,    # Уменьшено расстояние между элементами
                        expand=True,
                        max_extent=160, # Уменьшена максимальная ширина элемента
                    ),
                    ft.ElevatedButton("Назад", on_click=lambda e: e.page.go("/")),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )
