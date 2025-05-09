import reflex as rx
from about.styles import Size
from about.constants import MAX_WIDTH
from about.components.markdown import MARKDOWN_STYLES

def markdown_content(path: str) -> rx.Component:
    """Reusable markdown content component.
    
    Args:
        path (str): Path to content
    """
    return rx.box(
        rx.markdown(
            open(path).read(),
            component_map=MARKDOWN_STYLES["component_map"],
            css=MARKDOWN_STYLES["base"],
        ),
        width=["90%", "80%", "80%", "55%"],
        max_width=MAX_WIDTH,
        margin_x="auto",
        padding_x=Size.SMALL.value,
    )