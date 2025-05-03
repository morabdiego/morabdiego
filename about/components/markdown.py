import reflex as rx
from about.styles.styles import AltTextColor, Size

def heading(level: str, children) -> rx.Component:
    return rx.heading(
        children,
        as_=level,
        color=AltTextColor.PRIMARY.value if level != "h1" else AltTextColor.UNEXPECTED.value,
        font_size=Size.VERY_BIG.value if level == "h1" else 
                 Size.BIG.value if level == "h2" else 
                 Size.MEDIUM.value if level == "h3" else 
                 Size.DEFAULT.value,  # h4 size
        font_weight="normal" if level == "h4" else "bold",  # h4 not bold
        font_style="italic" if level == "h4" else "normal",  # h4 italic
        margin_bottom="1em" if level == "h1" else "0.8em",
        text_align="center" if level == "h1" else "left",
    )

def p(children) -> rx.Component:
    return rx.text(
        children,
        color=AltTextColor.PRIMARY.value,
        font_size=Size.DEFAULT.value,
        margin_bottom="1em",
        text_align="justify",
    )

def a(children) -> rx.Component:
    return rx.link(
        children,
        color=AltTextColor.ACCENT.value,
        text_decoration="none",
        font_weight="bold",
        _hover={"text_decoration": "underline"},
    )

def li(children) -> rx.Component:
    return rx.list_item(
        children,
        color=AltTextColor.PRIMARY.value,
        font_size=Size.DEFAULT.value,
        margin_bottom="1em",
        text_align="justify",
    )

MARKDOWN_STYLES = {
    "base": {
        "width": "100%",
        "maxWidth": "600px",
        "margin": "0 auto",
    },
    "component_map": {
        "h1": lambda children: heading("h1", children),
        "h2": lambda children: heading("h2", children),
        "h3": lambda children: heading("h3", children),
        "h4": lambda children: heading("h4", children),  # Added h4 support
        "p": p,
        "a": a,
        "li": li,  # Add list item support
    }
}