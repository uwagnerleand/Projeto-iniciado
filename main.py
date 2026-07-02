import flet as ft


def main(page: ft.Page):
    page.title = "Projeto Flet"
    page.add(ft.Text("Projeto iniciado"))


ft.app(target=main)