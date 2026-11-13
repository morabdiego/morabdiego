import reflex as rx
from about.styles.styles import (
    Color,
    AltColor,
    AltTextColor,
    Font,
    CARD_STYLE,
)
from about.constants import (
    SOCIAL_LINKS,
    GMAIL_URL,
    CV_PDF_ES_PATH,
    CV_PDF_EN_PATH,
    LOCATION_ES,
    LOCATION_EN,
    asset_url,
)
from about.data import PROFILE, HIGHLIGHTS
from about.state import is_spanish, t


def social_link_item(
    url: str, icon: str, label: str, desc_es: str, desc_en: str
) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.el.a(
                rx.image(
                    src=asset_url(f"/{icon}"),
                    alt=label,
                    width="20px",
                    height="20px",
                ),
                href=url,
                target="_blank",
                rel="noopener noreferrer",
                aria_label=label,
                style={
                    "display": "inline-flex",
                    "align_items": "center",
                    "justify_content": "center",
                    "width": "44px",
                    "height": "44px",
                    "border_radius": "12px",
                    "background": AltColor.CARD_BG.value,
                    "border": f"1px solid {AltColor.BORDER_STRONG.value}",
                    "box_shadow": "0 2px 8px rgba(30, 30, 30, 0.05)",
                    "transition": "all 0.2s ease",
                },
                _hover={
                    "transform": "translateY(-3px)",
                    "border_color": Color.ACCENT.value,
                    "background": "#ffffff",
                    "box_shadow": "0 8px 18px rgba(30, 30, 30, 0.10)",
                },
            ),
        ),
        rx.hover_card.content(
            rx.text(
                t(desc_es, desc_en),
                font_family=Font.BODY.value,
                color=AltTextColor.PRIMARY.value,
                font_size="0.82rem",
                font_weight="600",
            ),
            style={
                "background": AltColor.CARD_BG.value,
                "border": f"1px solid {AltColor.BORDER_STRONG.value}",
                "padding": "0.5rem 0.85rem",
                "border_radius": "10px",
                "box_shadow": "0 10px 24px rgba(30, 30, 30, 0.12)",
            },
        ),
    )


def profile_card() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.image(
                src=asset_url("/profile.jpg"),
                alt=PROFILE["name"],
                width=["170px", "200px", "220px"],
                height=["170px", "200px", "220px"],
                border_radius="50%",
                object_fit="cover",
                border=f"4px solid {AltColor.CARD_BG.value}",
                box_shadow=f"0 0 0 2px {Color.ACCENT.value}, 0 12px 28px -8px rgba(30, 30, 30, 0.16)",
            ),
            position="relative",
        ),
        rx.hstack(
            rx.icon("map-pin", size=15, color=AltTextColor.UNEXPECTED.value),
            rx.text(
                t(LOCATION_ES, LOCATION_EN),
                font_family=Font.BODY.value,
                font_size="0.82rem",
                font_weight="600",
                color=AltTextColor.MUTED.value,
            ),
            spacing="2",
            align="center",
            padding="0.35rem 0.85rem",
            border_radius="999px",
            background=AltColor.CARD_BG.value,
            border=f"1px solid {AltColor.BORDER.value}",
        ),
        rx.hstack(
            *[
                social_link_item(url, icon, label, desc_es, desc_en)
                for url, icon, label, desc_es, desc_en in SOCIAL_LINKS
            ],
            spacing="3",
            align="center",
            justify="center",
            style={"gap": "0.75rem"},
        ),
        align="center",
        spacing="4",
        flex_shrink="0",
    )


def highlight_card(item: dict) -> rx.Component:
    metric_text = (
        t(item["metric"], item["metric_en"])
        if "metric_en" in item
        else item["metric"]
    )
    return rx.box(
        rx.vstack(
            rx.text(
                metric_text,
                font_family=Font.HEADING.value,
                font_size=["1.65rem", "1.95rem"],
                font_weight="700",
                color=AltTextColor.UNEXPECTED.value,
                line_height="1.1",
                letter_spacing="-0.025em",
                style={"fontVariantNumeric": "tabular-nums"},
            ),
            rx.text(
                t(item["label_es"], item["label_en"]),
                font_family=Font.BODY.value,
                font_weight="700",
                font_size="0.92rem",
                color=AltTextColor.PRIMARY.value,
                margin_top="0.25rem",
            ),
            rx.text(
                t(item["detail_es"], item["detail_en"]),
                font_family=Font.BODY.value,
                font_size="0.83rem",
                font_weight="500",
                color=AltTextColor.MUTED.value,
                line_height="1.55",
            ),
            align="start",
            spacing="1",
        ),
        style={
            "padding": "1.25rem 0 0.25rem 0",
            "border_top": f"2px solid {Color.ACCENT.value}",
        },
        width="100%",
    )


def header() -> rx.Component:
    cv_href = rx.cond(
        is_spanish.value,
        asset_url(CV_PDF_ES_PATH),
        asset_url(CV_PDF_EN_PATH),
    )

    return rx.vstack(
        rx.flex(
            profile_card(),
            rx.vstack(
                # Editorial Role Eyebrow
                rx.hstack(
                    rx.box(
                        width="18px",
                        height="2px",
                        background=AltTextColor.UNEXPECTED.value,
                        flex_shrink="0",
                    ),
                    rx.text(
                        t(PROFILE["role_es"], PROFILE["role_en"]),
                        font_family=Font.BODY.value,
                        font_size="0.75rem",
                        font_weight="700",
                        text_transform="uppercase",
                        letter_spacing="0.11em",
                        color=AltTextColor.UNEXPECTED.value,
                    ),
                    spacing="2",
                    align="center",
                ),
                # Name & Tagline
                rx.vstack(
                    rx.heading(
                        PROFILE["name"],
                        as_="h1",
                        font_family=Font.HEADING.value,
                        font_size=["2.15rem", "2.75rem", "3.2rem"],
                        font_weight="800",
                        color=AltTextColor.PRIMARY.value,
                        line_height="1.1",
                        letter_spacing="-0.025em",
                    ),
                    rx.text(
                        t(PROFILE["tagline_es"], PROFILE["tagline_en"]),
                        font_family=Font.HEADING.value,
                        font_style="italic",
                        font_size=["1.02rem", "1.14rem"],
                        font_weight="500",
                        color=AltTextColor.SECONDARY.value,
                        line_height="1.45",
                    ),
                    spacing="2",
                    align="start",
                    width="100%",
                ),
                # Bio Paragraphs (optimal 65ch reading measure)
                rx.vstack(
                    rx.text(
                        t(PROFILE["bio_p1_es"], PROFILE["bio_p1_en"]),
                        font_family=Font.BODY.value,
                        font_size="0.96rem",
                        font_weight="500",
                        color=AltTextColor.PRIMARY.value,
                        line_height="1.75",
                        max_width="65ch",
                    ),
                    rx.text(
                        t(PROFILE["bio_p2_es"], PROFILE["bio_p2_en"]),
                        font_family=Font.BODY.value,
                        font_size="0.94rem",
                        font_weight="400",
                        color=AltTextColor.MUTED.value,
                        line_height="1.75",
                        max_width="65ch",
                    ),
                    spacing="3",
                    align="start",
                    width="100%",
                ),
                # Action CTA Buttons
                rx.flex(
                    rx.el.a(
                        rx.hstack(
                            rx.icon("download", size=17),
                            rx.text(
                                t("Descargar CV (PDF)", "Download CV (PDF)"),
                                font_family=Font.BODY.value,
                                font_weight="700",
                                font_size="0.86rem",
                            ),
                            spacing="2",
                            align="center",
                        ),
                        href=cv_href,
                        target="_blank",
                        rel="noopener noreferrer",
                        style={
                            "display": "inline-flex",
                            "align_items": "center",
                            "justify_content": "center",
                            "background": Color.BACKGROUND.value,
                            "color": Color.PRIMARY.value,
                            "padding": "0.75rem 1.35rem",
                            "border_radius": "10px",
                            "text_decoration": "none",
                            "border": f"1.5px solid {Color.BACKGROUND.value}",
                            "transition": "all 0.2s ease",
                        },
                        _hover={
                            "background": Color.ACCENT.value,
                            "color": Color.BACKGROUND_DEEP.value,
                            "border_color": Color.ACCENT.value,
                            "transform": "translateY(-1px)",
                        },
                    ),
                    rx.el.a(
                        rx.hstack(
                            rx.icon("briefcase", size=17),
                            rx.text(
                                t("Ver experiencia", "View Experience & CV"),
                                font_family=Font.BODY.value,
                                font_weight="700",
                                font_size="0.86rem",
                            ),
                            spacing="2",
                            align="center",
                        ),
                        href="#experience",
                        style={
                            "display": "inline-flex",
                            "align_items": "center",
                            "justify_content": "center",
                            "background": AltColor.CARD_BG.value,
                            "color": AltTextColor.PRIMARY.value,
                            "padding": "0.75rem 1.35rem",
                            "border_radius": "10px",
                            "text_decoration": "none",
                            "border": f"1px solid {AltColor.BORDER_STRONG.value}",
                            "transition": "all 0.2s ease",
                        },
                        _hover={
                            "border_color": Color.ACCENT.value,
                            "background": "#ffffff",
                            "transform": "translateY(-1px)",
                        },
                    ),
                    rx.el.a(
                        rx.hstack(
                            rx.icon("mail", size=17),
                            rx.text(
                                t("Contactar", "Contact Me"),
                                font_family=Font.BODY.value,
                                font_weight="700",
                                font_size="0.86rem",
                            ),
                            spacing="2",
                            align="center",
                        ),
                        href=GMAIL_URL,
                        style={
                            "display": "inline-flex",
                            "align_items": "center",
                            "justify_content": "center",
                            "background": AltColor.ACCENT_SOFT.value,
                            "color": AltTextColor.SECONDARY.value,
                            "padding": "0.75rem 1.25rem",
                            "border_radius": "10px",
                            "text_decoration": "none",
                            "border": "1px solid rgba(36, 106, 76, 0.28)",
                            "transition": "all 0.2s ease",
                        },
                        _hover={
                            "background": Color.ACCENT.value,
                            "color": Color.BACKGROUND_DEEP.value,
                            "transform": "translateY(-1px)",
                        },
                    ),
                    spacing="4",
                    wrap="wrap",
                    align="center",
                    style={
                        "gap": "1rem",
                        "paddingTop": "0.6rem",
                    },
                ),
                spacing="4",
                align="start",
                width="100%",
            ),
            direction=rx.breakpoints(initial="column", md="row"),
            spacing="7",
            align="center",
            width="100%",
            style={"gap": "2.75rem"},
        ),
        # Key Metrics / Highlights Row
        rx.grid(
            *[highlight_card(item) for item in HIGHLIGHTS],
            columns=rx.breakpoints(initial="1", sm="3", md="3"),
            spacing="5",
            width="100%",
            style={"gap": "1.25rem", "paddingTop": "1.25rem"},
        ),
        spacing="6",
        width="100%",
    )
