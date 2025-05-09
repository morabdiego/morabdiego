import reflex as rx
from about.styles import Color

def footer() -> rx.Component:
    """Footer con texto alineado a la derecha."""
    return rx.box(
        "Copyright 2025 (c). | Diego Mora",
        font_size="14px",
        text_align="right",
        padding="1rem",
        width="100%",
        position="fixed",
        bottom="0",
        background=Color.BACKGROUND.value,  # Añadimos un fondo para que se vea bien
        z_index="1000",
    )