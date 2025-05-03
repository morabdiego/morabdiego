import reflex as rx
from about.styles.styles import Color, TextColor, Size
from about.constants import NAV_LINKS_EN, NAV_LINKS_ES
from about.components.ant_components import float_button
from about.components.lang_button import language_switch
from about.state import State

def nav_item(text: str, url: str) -> rx.Component:
    return rx.link(
        text,
        href=url,
        color=TextColor.PRIMARY.value,
        font_weight="bold",
        # font_size=Size.MEDIUM.value,
        _hover={"color": TextColor.SECONDARY.value},
    )

def get_nav_links() -> list:
    return rx.cond(
        State.is_spanish,
        NAV_LINKS_ES,
        NAV_LINKS_EN
    )

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # float_button(),
            rx.hstack(
                rx.foreach(
                    get_nav_links(),
                    lambda item: nav_item(item[0], item[1])
                ),
                padding_x=[Size.DEFAULT.value, Size.BIG.value, Size.VERY_BIG.value, Size.HUGE.value],
                spacing="6",
                #gap="4",
            ),
            rx.hstack(
                language_switch(),
                width="100%",
                justify_content="flex-end",
                padding_x=[Size.DEFAULT.value, Size.BIG.value, Size.VERY_BIG.value, Size.HUGE.value]
            ),
            width="100%",
            bg=Color.BACKGROUND.value,
            border_bottom=f"0.25em solid {Color.ACCENT.value}",
            padding_y=[Size.SMALL.value, Size.DEFAULT.value],
            #align_items="center",
        )
    )
