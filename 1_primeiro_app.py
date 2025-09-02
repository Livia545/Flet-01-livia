# Primeiro programa desenvolvido em python

import flet as ft

def main(page: ft.Page):

    # Configurações básicas da página
    page.title = "Meu Primeiro App Flet"
    page.padding = 20

    meu_texto = ft.Text(
        value = "🎉 Hello world! (Primeiro app com Flet!)",
        size = 24,
        color = ft.Colors.BLUE,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.CENTER
    )
    page.add(meu_texto)

    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile!", size = 16),
        ft.Text("Com Flet, você pode criar apps incríveis! 📱", size = 16, color = ft.Colors.GREEN)
    )

ft.app(target=main)
