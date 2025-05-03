import reflex as rx
from about.styles.styles import Size, AltTextColor  # Import ACCENT color
from about.constants import SOCIAL_LINKS, MAX_WIDTH

def profile_image() -> rx.Component:
    return rx.image(
        src="/profile.jpg",
        width=["150px", "175px", "200px"],  # Responsive sizes
        height=["150px", "175px", "200px"],  # Responsive sizes
        border_radius="50%",
        object_fit="cover",
        box_shadow="lg",
        margin_right=Size.VERY_BIG.value,
    )

def social_link_item(url: str, icon: str, description: str) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.link(
                rx.image(
                    src=f"/{icon}",
                    width="30px",
                    height="30px",
                ),
                href=url,
                is_external=True,
            ),
        ),
        rx.hover_card.content(
            rx.text(
                description,
                color=AltTextColor.ACCENT.value,
                font_size=Size.DEFAULT.value,
            ),
        ),
    )

def header() -> rx.Component:
    return rx.hstack(
        profile_image(),
        rx.vstack(
            rx.text(
                "About",
                font_size=Size.VERY_BIG.value,  # Responsive font size
                color=AltTextColor.UNEXPECTED.value,
                font_weight="bold",
            ),
            rx.text(
                "@morabdiego",
                font_size=Size.BIG.value,  # Responsive font size
                color=AltTextColor.PRIMARY.value,
                font_weight="bold",
            ),
            rx.hstack(
                *[
                    social_link_item(url, icon, text) for url, icon, text in SOCIAL_LINKS
                ],
                spacing="6",
                align_items="center",
            ),
            spacing="1"  # Numeric spacing between elements
        ),
        spacing="3",  # Numeric spacing between profile image and text
        align_items="center",
        justify_content="center",
        width="100%",
        padding=Size.MEDIUM.value,
        max_width=MAX_WIDTH,
        margin_x="auto",
        flex_direction=["column", "row"],  # Responsive layout
    )
