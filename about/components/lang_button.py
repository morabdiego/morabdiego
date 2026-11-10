import reflex as rx
from about.state import is_spanish
from about.styles.styles import Color, TextColor, Font


def language_switch() -> rx.Component:
    """Client-side ES / EN toggle pill (zero backend required)."""
    return rx.hstack(
        rx.el.button(
            "ES",
            type="button",
            on_click=is_spanish.set_value(True),
            style={
                "padding": "0.35rem 0.75rem",
                "border_radius": "999px",
                "font_family": Font.BODY.value,
                "font_size": "0.78rem",
                "font_weight": "700",
                "letter_spacing": "0.04em",
                "cursor": "pointer",
                "border": "none",
                "transition": "all 0.2s ease",
                "background": rx.cond(
                    is_spanish.value, Color.ACCENT.value, "transparent"
                ),
                "color": rx.cond(
                    is_spanish.value,
                    Color.BACKGROUND_DEEP.value,
                    TextColor.PRIMARY.value,
                ),
            },
        ),
        rx.el.button(
            "EN",
            type="button",
            on_click=is_spanish.set_value(False),
            style={
                "padding": "0.35rem 0.75rem",
                "border_radius": "999px",
                "font_family": Font.BODY.value,
                "font_size": "0.78rem",
                "font_weight": "700",
                "letter_spacing": "0.04em",
                "cursor": "pointer",
                "border": "none",
                "transition": "all 0.2s ease",
                "background": rx.cond(
                    is_spanish.value, "transparent", Color.ACCENT.value
                ),
                "color": rx.cond(
                    is_spanish.value,
                    TextColor.PRIMARY.value,
                    Color.BACKGROUND_DEEP.value,
                ),
            },
        ),
        spacing="1",
        align="center",
        padding="4px",
        background=Color.SURFACE.value,
        border=f"1px solid {Color.BORDER.value}",
        border_radius="999px",
    )
