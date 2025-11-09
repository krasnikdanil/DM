import flet as ft

def RationalView():
    return ft.View(
        "/rational",
        [
            ft.AppBar(title=ft.Text("Rational Numbers"), bgcolor=ft.Colors.ON_SURFACE_VARIANT),
            ft.Text("This is the Rational Numbers page."),
            ft.ElevatedButton("Go back", on_click=lambda e: e.page.go("/")),
        ]
    )
