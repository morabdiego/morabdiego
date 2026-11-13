import reflex as rx
from about.styles.styles import Color, TextColor, Font
from about.constants import NAV_SECTIONS, MAX_WIDTH
from about.components.lang_button import language_switch
from about.state import t, mobile_menu_open


def nav_anchor_item(href: str, label_es: str, label_en: str) -> rx.Component:
    return rx.el.a(
        t(label_es, label_en),
        href=href,
        on_click=mobile_menu_open.set_value(False),
        style={
            "display": "inline-flex",
            "align_items": "center",
            "justify_content": "between",
            "width": "100%",
            "color": TextColor.PRIMARY.value,
            "font_family": Font.BODY.value,
            "font_size": "0.92rem",
            "font_weight": "600",
            "letter_spacing": "0.01em",
            "text_decoration": "none",
            "white_space": "nowrap",
            "padding": "0.65rem 0.9rem",
            "border_radius": "10px",
            "transition": "all 0.2s ease",
        },
        _hover={
            "color": Color.ACCENT.value,
            "background": "rgba(100, 182, 146, 0.12)",
        },
    )


def menu_toggle_button() -> rx.Component:
    return rx.el.button(
        rx.cond(
            mobile_menu_open.value,
            rx.icon("x", size=20, color=TextColor.PRIMARY.value),
            rx.icon("menu", size=20, color=TextColor.PRIMARY.value),
        ),
        type="button",
        aria_label="Toggle navigation menu",
        on_click=mobile_menu_open.set_value(
            rx.cond(mobile_menu_open.value, False, True)
        ),
        style={
            "display": "inline-flex",
            "align_items": "center",
            "justify_content": "center",
            "width": "40px",
            "height": "40px",
            "border_radius": "10px",
            "background": "rgba(255, 255, 255, 0.08)",
            "border": "1px solid rgba(240, 238, 220, 0.18)",
            "cursor": "pointer",
            "transition": "all 0.2s ease",
        },
        _hover={
            "border_color": Color.ACCENT.value,
            "background": "rgba(100, 182, 146, 0.18)",
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
                            font_weight="700",
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
                    on_click=mobile_menu_open.set_value(False),
                    style={
                        "display": "inline-flex",
                        "align_items": "center",
                        "text_decoration": "none",
                    },
                ),
                # Right Control: Always-visible Menu Toggle Button
                menu_toggle_button(),
                justify="between",
                align="center",
                width="100%",
                max_width=MAX_WIDTH,
                margin_x="auto",
                padding_x=["1.25rem", "2rem", "3rem"],
                padding_y="0.9rem",
            ),
            # Collapsible Dropdown Menu (all screen sizes)
            rx.cond(
                mobile_menu_open.value,
                rx.box(
                    rx.vstack(
                        *[
                            nav_anchor_item(href, es, en)
                            for href, es, en in NAV_SECTIONS
                        ],
                        rx.hstack(
                            rx.text(
                                t("Idioma", "Language"),
                                font_family=Font.BODY.value,
                                font_size="0.88rem",
                                font_weight="600",
                                color=TextColor.MUTED.value,
                            ),
                            language_switch(),
                            justify="between",
                            align="center",
                            width="100%",
                            padding_top="0.65rem",
                            margin_top="0.25rem",
                            border_top=f"1px solid {Color.BORDER.value}",
                        ),
                        spacing="1",
                        align="start",
                        width="100%",
                        max_width=MAX_WIDTH,
                        margin_x="auto",
                        padding_x=["1.25rem", "2rem", "3rem"],
                        padding_top="0.5rem",
                        padding_bottom="1rem",
                    ),
                    width="100%",
                    border_top=f"1px solid {Color.BORDER.value}",
                ),
            ),
            width="100%",
            style={
                "background": "rgba(24, 24, 24, 0.66)",
                "backdrop_filter": "blur(20px) saturate(160%)",
                "-webkit-backdrop-filter": "blur(20px) saturate(160%)",
                "border_bottom": "1px solid rgba(100, 182, 146, 0.45)",
                "box_shadow": "inset 0 -1px 0 rgba(255, 255, 255, 0.08), 0 8px 32px rgba(20, 20, 20, 0.14)",
            },
        ),
        style={
            "position": "sticky",
            "top": "0",
            "z_index": "1000",
            "width": "100%",
        },
    )
