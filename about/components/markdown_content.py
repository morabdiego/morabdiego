import reflex as rx
from about.styles.styles import Size, AltTextColor
from about.constants import MAX_WIDTH
from about.components.markdown import MARKDOWN_STYLES
from about.state import State

def get_content(es_path: str, en_path: str) -> str:
    """Get content based on language state.
    
    Args:
        es_path (str): Path to Spanish content
        en_path (str): Path to English content
    """
    return rx.cond(
        State.is_spanish,
        open(es_path).read(),
        open(en_path).read()
    )

def markdown_content(es_path: str, en_path: str) -> rx.Component:
    """Reusable markdown content component.
    
    Args:
        es_path (str): Path to Spanish content
        en_path (str): Path to English content
    """
    return rx.box(
        rx.markdown(
            get_content(es_path, en_path),
            component_map=MARKDOWN_STYLES["component_map"],
            css=MARKDOWN_STYLES["base"],
        ),
        width=["90%", "80%", "80%", "55%"],
        max_width=MAX_WIDTH,
        margin_x="auto",
        padding_x=Size.SMALL.value,
    )