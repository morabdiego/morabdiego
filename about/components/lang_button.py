import reflex as rx
from about.state import State
from about.styles.styles import Size

def language_switch() -> rx.Component:
    return rx.hstack(
        rx.segmented_control.root(
            rx.segmented_control.item("EN", value="EN"),
            rx.segmented_control.item("ES", value="ES"),
            value=rx.cond(
                State.is_spanish,
                "ES",
                "EN"
            ),
            on_change=State.toggle_language,
        ),
        margin_right=Size.MEDIUM.value,
    )