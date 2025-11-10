import flet as ft

def PolynomialView():
    return ft.View(
        "/polynomial",
        [
            ft.AppBar(title=ft.Text("Polynomials"), bgcolor=ft.Colors.ON_SURFACE_VARIANT),
            ft.Text("This is the Polynomials page."),
            ft.ElevatedButton("Go back", on_click=lambda e: e.page.go("/")),
        ]
    )
