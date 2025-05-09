import reflex as rx
from about.styles import Size
from about.constants import MAX_WIDTH, PUBLICATIONS_MD
from about.components.layout import layout
from about.components.markdown_content import markdown_content

@rx.page("/publications", title="Publications")
def publications() -> rx.Component:
    return layout(
        rx.box(
            markdown_content(PUBLICATIONS_MD),
            width="100%",
            max_width=MAX_WIDTH,
            margin_x="auto",
            padding_top=Size.VERY_BIG.value,
            padding_bottom=Size.VERY_BIG.value,
            align_items="center",
        )
    )