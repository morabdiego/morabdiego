import reflex as rx
from about.styles.styles import Size, AltColor
from about.components.navbar import navbar
from about.components.footer import footer
from about.constants import MAX_WIDTH, PUBLICATIONS_MD_EN, PUBLICATIONS_MD_ES
from about.components.markdown_content import markdown_content

@rx.page(route="/publications", title="morabdiego | Publications")
def publications() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.box(
                markdown_content(PUBLICATIONS_MD_ES, PUBLICATIONS_MD_EN),
                width="100%",
                max_width=MAX_WIDTH,
                margin_x="auto",
                padding_y=Size.VERY_BIG.value,
                min_height="calc(100vh - 140px)",
                align_items="center",
            ),
            width="100%",
            background=AltColor.BACKGROUND.value,
        ),
        footer(),
        width="100%"
    )