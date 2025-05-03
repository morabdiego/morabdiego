import reflex as rx
from about.styles.styles import Size, AltColor
from about.constants import MAX_WIDTH, ABOUT_MD_EN, ABOUT_MD_ES
from about.components.header import header
from about.components.markdown_content import markdown_content

def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.vstack(
                    header(),
                    markdown_content(ABOUT_MD_ES, ABOUT_MD_EN),
                    spacing="9",
                ),
                width="100%",
                max_width=MAX_WIDTH,
                margin_x="auto",
                padding_x=[
                    Size.DEFAULT.value,
                    Size.MEDIUM.value,
                    Size.VERY_BIG.value,
                    Size.VERY_BIG.value
                ],
                align_items="center",
                padding_y=Size.VERY_BIG.value,
                min_height="calc(100vh - 110px)",
            ),
            width="100%",
            background=AltColor.BACKGROUND.value,
        ),
        width="100%",
    )
