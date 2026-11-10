import reflex as rx
from about.styles.styles import AltColor
from about.constants import MAX_WIDTH
from about.components.header import header


def hero() -> rx.Component:
    return rx.el.section(
        rx.box(
            header(),
            width="100%",
            max_width=MAX_WIDTH,
            margin_x="auto",
            padding_x=["1.25rem", "2rem", "3rem"],
            padding_y=["3rem", "4.5rem", "5.5rem"],
        ),
        id="about",
        style={
            "width": "100%",
            "background": AltColor.BACKGROUND.value,
        },
    )
