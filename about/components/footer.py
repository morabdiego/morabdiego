import reflex as rx
from about.styles.styles import Size, Color, TextColor
from about.constants import SOCIAL_LINKS, FULL_WIDTH, COPYRIGHT_EN, COPYRIGHT_ES
from about.state import State

def get_copyright() -> str:
    return rx.cond(
        State.is_spanish,
        COPYRIGHT_ES,
        COPYRIGHT_EN
    )


def footer() -> rx.Component:
    return rx.vstack(
        # rx.flex(
        #     *[
        #         social_link_item(text, url, icon) for text, url, icon in SOCIAL_LINKS
        #     ],
        #     spacing="5",
        #     padding_x=Size.SMALL.value,
        #     align_items="center",
        #     justify_content="center",
        #     flex_direction=["column", "column", "column", "row"],
        #     flex_wrap="wrap",
        #     gap="4",
        #     width="100%",
        # ),
        rx.text(
            get_copyright(),
            color=TextColor.PRIMARY.value,
            font_size=Size.SMALL.value,
            white_space="nowrap",
            padding_top="4",
            padding_right=Size.SMALL.value,
        ),
        width="100%",
        max_width=FULL_WIDTH,
        margin_x="auto",
        bg=Color.BACKGROUND.value,
        border_top=f"0.25em solid {Color.ACCENT.value}",
        padding_x=[Size.DEFAULT.value, Size.MEDIUM.value, Size.BIG.value, Size.HUGE.value],
        padding_y=Size.SMALL.value,
        spacing="4",
        align_items="center",
    )
