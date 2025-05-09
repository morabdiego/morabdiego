import reflex as rx
from about.styles import AltColor
from about.components.navbar import navbar
from about.components.footer import footer
from about.constants import MAX_WIDTH

def layout(*children: rx.Component) -> rx.Component:
    """General layout component with consistent styling."""
    return rx.box(
        rx.vstack(
            navbar(),
            rx.box(
                rx.vstack(
                    *children,
                    width="100%",
                    max_width=MAX_WIDTH,
                    margin_x="auto",
                    min_height="calc(100vh - 140px)",  # Account for navbar and footer
                ),
                width="100%",
                background=AltColor.BACKGROUND.value,
                margin_top="60px",  # Space for navbar
                padding_bottom="60px",  # Space for footer
            ),
            footer(),
        ),
        width="100%",
    )
