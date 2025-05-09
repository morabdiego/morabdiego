import reflex as rx
from about.styles import Color, TextColor, Size

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.link(
                    "Inicio",
                    href="/",
                    color=TextColor.PRIMARY.value,
                    font_weight="bold",
                    _hover={"color": TextColor.SECONDARY.value},
                ),
                rx.link(
                    "Publicaciones",
                    href="/publications",
                    color=TextColor.PRIMARY.value,
                    font_weight="bold",
                    _hover={"color": TextColor.SECONDARY.value},
                ),
                padding_x=[Size.DEFAULT.value, Size.BIG.value, Size.VERY_BIG.value, Size.HUGE.value],
                spacing="6",
            ),
            width="100%",
            bg=Color.BACKGROUND.value,
            border_bottom=f"0.25em solid {Color.ACCENT.value}",
            padding_y=[Size.SMALL.value, Size.DEFAULT.value],
        ),
        position="fixed",
        top="0",
        width="100%",
        z_index="1000",
    )
