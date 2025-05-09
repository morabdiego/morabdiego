import reflex as rx
from about.components.layout import layout
from about.components.hero import hero

@rx.page("/", title="Diego Mora")
def index() -> rx.Component:
    return layout(
        hero(),
    )