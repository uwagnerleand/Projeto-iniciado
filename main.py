import asyncio
import time

import flet as ft


async def main(page: ft.Page):
    page.title = "Projeto Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30
    page.window.width = 500
    page.window.height = 700

    # ── Status ──────────────────────────────────────────────
    status_text = ft.Text(
        value="👋 Aguardando ação...",
        size=16,
        text_align=ft.TextAlign.CENTER,
    )

    progress_ring = ft.ProgressRing(
        width=50,
        height=50,
        stroke_width=4,
        visible=False,
    )

    # ── Test interaction counter ────────────────────────────
    test_counter = 0
    test_feedback = ft.Text(
        value="",
        size=14,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREEN,
    )

    # ── Sync handler ────────────────────────────────────────
    def on_click_sync(e):
        btn_sync.disabled = True
        status_text.value = "⏳ Processamento síncrono iniciado — a interface congelou por 5s..."
        progress_ring.visible = True
        page.update()

        time.sleep(5)

        status_text.value = "✅ Processamento síncrono finalizado! (interface ficou travada)"
        progress_ring.visible = False
        btn_sync.disabled = False
        page.update()

    # ── Async handler ───────────────────────────────────────
    async def on_click_async(e):
        btn_async.disabled = True
        status_text.value = "⏳ Processamento assíncrono iniciado — interface continua responsiva..."
        progress_ring.visible = True
        page.update()

        await asyncio.sleep(5)

        status_text.value = "✅ Processamento assíncrono finalizado! (interface ficou livre)"
        progress_ring.visible = False
        btn_async.disabled = False
        page.update()

    # ── Test handler ────────────────────────────────────────
    def on_click_test(e):
        nonlocal test_counter
        test_counter += 1
        test_feedback.value = f"🔵 Interatividade OK! Clique nº {test_counter}"
        test_feedback.color = ft.Colors.GREEN if test_counter % 2 == 1 else ft.Colors.ORANGE
        status_text.value = "✅ Teste de interatividade realizado com sucesso!"
        page.update()

    # ── Buttons ─────────────────────────────────────────────
    btn_sync = ft.Button(
        content=ft.Text("Processar Áudio (Síncrono)", size=15),
        on_click=on_click_sync,
        width=300,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.RED_700,
        ),
    )

    btn_async = ft.Button(
        content=ft.Text("Processar Áudio (Assíncrono)", size=15),
        on_click=on_click_async,
        width=300,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE_700,
        ),
    )

    btn_test = ft.Button(
        content=ft.Text("Testar Interatividade", size=15),
        on_click=on_click_test,
        width=300,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.GREEN_700,
        ),
    )

    # ── Layout ──────────────────────────────────────────────
    page.add(
        ft.Column(
            controls=[
                # Title
                ft.Container(
                    content=ft.Text(
                        value="⚡ Síncrono vs Assíncrono",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    margin=ft.margin.only(bottom=4),
                ),
                ft.Text(
                    value="Compare o comportamento de chamadas síncronas e assíncronas",
                    size=13,
                    color=ft.Colors.GREY_600,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(height=24, color=ft.Colors.TRANSPARENT),

                # Sync block
                ft.Container(
                    content=ft.Column(
                        controls=[
                            btn_sync,
                            ft.Text(
                                value="⛔ Bloqueia a interface por 5 segundos",
                                size=12,
                                color=ft.Colors.GREY_500,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=4,
                    ),
                ),
                ft.Divider(height=16, color=ft.Colors.TRANSPARENT),

                # Async block
                ft.Container(
                    content=ft.Column(
                        controls=[
                            btn_async,
                            ft.Text(
                                value="✅ Mantém a interface responsiva",
                                size=12,
                                color=ft.Colors.GREY_500,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=4,
                    ),
                ),
                ft.Divider(height=16, color=ft.Colors.TRANSPARENT),

                # Test block
                ft.Container(
                    content=ft.Column(
                        controls=[
                            btn_test,
                            test_feedback,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=4,
                    ),
                ),
                ft.Divider(height=24, color=ft.Colors.TRANSPARENT),

                # Progress & status
                progress_ring,
                ft.Divider(height=12, color=ft.Colors.TRANSPARENT),
                status_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        )
    )


ft.run(main)