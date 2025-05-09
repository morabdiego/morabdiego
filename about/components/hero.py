import reflex as rx
from about.styles import Size
from about.constants import MAX_WIDTH, ABOUT_MD
from about.components.header import header
from about.components.markdown_content import markdown_content

def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            header(),
            markdown_content(ABOUT_MD),
            spacing="9",
        ),
        width="100%",
        padding_x=[
            Size.DEFAULT.value,
            Size.MEDIUM.value,
            Size.VERY_BIG.value,
            Size.VERY_BIG.value
        ],
        padding_y=Size.VERY_BIG.value,
        align_items="center",
    )
