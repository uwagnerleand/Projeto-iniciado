import asyncio
import time

import flet as ft


async def main(page: ft.Page):
    page.title = "Projeto Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40

    status_text = ft.Text(
        value="Aguardando ação...",
        size=16,
        text_align=ft.TextAlign.CENTER,
    )

    progress_ring = ft.ProgressRing(
        width=50,
        height=50,
        stroke_width=4,
        visible=False,
    )

    def on_click_sync(e):
        status_text.value = "Processamento síncrono iniciado..."
        progress_ring.visible = True
        page.update()
        time.sleep(5)
        status_text.value = "Processamento síncrono finalizado!"
        progress_ring.visible = False
        page.update()

    async def on_click_async(e):
        status_text.value = "Processamento assíncrono iniciado..."
        progress_ring.visible = True
        page.update()
        await asyncio.sleep(5)
        status_text.value = "Processamento assíncrono finalizado!"
        progress_ring.visible = False
        page.update()

    def on_click_test(e):
        status_text.value = "Interatividade testada com sucesso!"
        progress_ring.visible = False
        page.update()

    btn_sync = ft.Button(
        content=ft.Text("Processar Áudio (Síncrono)"),
        on_click=on_click_sync,
        width=280,
    )

    btn_async = ft.Button(
        content=ft.Text("Processar Áudio (Assíncrono)"),
        on_click=on_click_async,
        width=280,
    )

    btn_test = ft.Button(
        content=ft.Text("Testar Interatividade"),
        on_click=on_click_test,
        width=280,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    value="Monitoramento de Áudio",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                btn_sync,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                btn_async,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                btn_test,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                progress_ring,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                status_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )
    )


ft.run(main)