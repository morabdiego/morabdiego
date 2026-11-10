import reflex as rx
from about.styles.styles import Color, TextColor, Font
from about.constants import NAV_SECTIONS, MAX_WIDTH
from about.components.lang_button import language_switch
from about.state import t


def nav_anchor_item(href: str, label_es: str, label_en: str) -> rx.Component:
    return rx.el.a(
        t(label_es, label_en),
        href=href,
        style={
            "display": "inline-flex",
            "align_items": "center",
            "color": TextColor.PRIMARY.value,
            "font_family": Font.BODY.value,
            "font_size": "0.88rem",
            "font_weight": "600",
            "letter_spacing": "0.01em",
            "text_decoration": "none",
            "white_space": "nowrap",
            "padding": "0.45rem 0.9rem",
            "border_radius": "999px",
            "transition": "all 0.2s ease",
        },
        _hover={
            "color": Color.ACCENT.value,
            "background": "rgba(100, 182, 146, 0.12)",
        },
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.box(
            rx.hstack(
                # Brand / Monogram
                rx.el.a(
                    rx.hstack(
                        rx.box(
                            width="10px",
                            height="10px",
                            border_radius="50%",
                            background=Color.ACCENT.value,
                            box_shadow=f"0 0 12px {Color.ACCENT.value}",
                            flex_shrink="0",
                        ),
                        rx.text(
                            "Diego Mora",
                            font_family=Font.HEADING.value,
                            font_weight="800",
                            font_size=["1.05rem", "1.2rem"],
                            color=TextColor.PRIMARY.value,
                            letter_spacing="-0.02em",
                        ),
                        # rx.text(
                        #     "@morabdiego",
                        #     font_family=Font.BODY.value,
                        #     font_size="0.8rem",
                        #     font_weight="500",
                        #     color=TextColor.MUTED.value,
                        #     display=["none", "inline", "inline"],
                        # ),
                        spacing="2",
                        align="center",
                    ),
                    href="#about",
                    style={
                        "display": "inline-flex",
                        "align_items": "center",
                        "text_decoration": "none",
                    },
                ),
                # Desktop Navigation Links
                rx.hstack(
                    *[
                        nav_anchor_item(href, es, en)
                        for href, es, en in NAV_SECTIONS
                    ],
                    spacing="2",
                    align="center",
                    display=["none", "none", "none", "flex"],
                ),
                # Right Control: Language Toggle only (CV button removed from navbar)
                rx.hstack(
                    language_switch(),
                    align="center",
                ),
                justify="between",
                align="center",
                width="100%",
                max_width=MAX_WIDTH,
                margin_x="auto",
                padding_x=["1.25rem", "2rem", "3rem"],
                padding_y="0.9rem",
            ),
            # Mobile / Tablet Secondary Section Bar
            rx.hstack(
                *[
                    nav_anchor_item(href, es, en)
                    for href, es, en in NAV_SECTIONS
                ],
                spacing="2",
                align="center",
                display=["flex", "flex", "flex", "none"],
                overflow_x="auto",
                width="100%",
                padding_x="1rem",
                padding_y="0.5rem",
                justify="center",
                border_top=f"1px solid {Color.BORDER.value}",
            ),
            width="100%",
            background="rgba(26, 26, 26, 0.95)",
            backdrop_filter="blur(14px)",
            border_bottom=f"3px solid {Color.ACCENT.value}",
        ),
        style={
            "position": "sticky",
            "top": "0",
            "z_index": "1000",
            "width": "100%",
        },
    )
