import reflex as rx
from about.styles.styles import Color, TextColor, Font
from about.constants import (
    MAX_WIDTH,
    COPYRIGHT_EN,
    COPYRIGHT_ES,
    GMAIL_ADDRESS,
    GMAIL_URL,
    LINKEDIN_URL,
    GITHUB_URL,
    INSTAGRAM_URL,
    CV_PDF_ES_PATH,
    CV_PDF_EN_PATH,
    asset_url,
)
from about.state import is_spanish, t


def footer_social_link(label: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.hstack(
            rx.text(
                label,
                font_family=Font.BODY.value,
                font_size="0.86rem",
                font_weight="600",
            ),
            rx.icon("arrow-up-right", size=14),
            spacing="1",
            align="center",
        ),
        href=url,
        target="_blank",
        rel="noopener noreferrer",
        style={
            "display": "inline-flex",
            "align_items": "center",
            "color": TextColor.MUTED.value,
            "text_decoration": "none",
            "padding": "0.3rem 0.6rem",
            "border_radius": "8px",
            "transition": "all 0.2s ease",
        },
        _hover={
            "color": Color.ACCENT.value,
            "background": "rgba(100, 182, 146, 0.10)",
        },
    )


def footer() -> rx.Component:
    cv_href = rx.cond(
        is_spanish.value,
        asset_url(CV_PDF_ES_PATH),
        asset_url(CV_PDF_EN_PATH),
    )

    return rx.el.footer(
        rx.box(
            rx.vstack(
                # Top Contact CTA Area
                rx.flex(
                    rx.vstack(
                        rx.text(
                            t("CONTACTO & COLABORACIÓN", "CONTACT & COLLABORATION"),
                            font_family=Font.BODY.value,
                            font_size="0.74rem",
                            font_weight="700",
                            letter_spacing="0.12em",
                            color=Color.ACCENT.value,
                        ),
                        rx.heading(
                            t(
                                "Contacta conmigo",
                                "Let’s talk.",
                            ),
                            as_="h2",
                            font_family=Font.HEADING.value,
                            font_size=["1.55rem", "1.95rem"],
                            font_weight="700",
                            color=TextColor.PRIMARY.value,
                            max_width="560px",
                            line_height="1.25",
                            letter_spacing="-0.02em",
                        ),
                        spacing="2",
                        align="start",
                    ),
                    rx.flex(
                        rx.el.a(
                            rx.hstack(
                                rx.icon("mail", size=17),
                                rx.text(
                                    GMAIL_ADDRESS,
                                    font_family=Font.BODY.value,
                                    font_weight="700",
                                    font_size="0.88rem",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            href=GMAIL_URL,
                            style={
                                "display": "inline-flex",
                                "align_items": "center",
                                "justify_content": "center",
                                "background": Color.ACCENT.value,
                                "color": Color.BACKGROUND_DEEP.value,
                                "padding": "0.8rem 1.45rem",
                                "border_radius": "12px",
                                "text_decoration": "none",
                                "transition": "all 0.2s ease",
                            },
                            _hover={"opacity": "0.92", "transform": "translateY(-2px)"},
                        ),
                        rx.el.a(
                            rx.hstack(
                                rx.icon("download", size=17),
                                rx.text(
                                    t("Descargar CV", "Download CV"),
                                    font_family=Font.BODY.value,
                                    font_weight="700",
                                    font_size="0.88rem",
                                    white_space="nowrap",
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
                                "min_width": "176px",
                                "background": "rgba(255, 255, 255, 0.07)",
                                "backdrop_filter": "blur(12px)",
                                "-webkit-backdrop-filter": "blur(12px)",
                                "color": TextColor.PRIMARY.value,
                                "padding": "0.8rem 1.45rem",
                                "border_radius": "12px",
                                "border": "1px solid rgba(240, 238, 220, 0.18)",
                                "text_decoration": "none",
                                "transition": "all 0.2s ease",
                            },
                            _hover={
                                "border_color": Color.ACCENT.value,
                                "color": Color.ACCENT.value,
                                "transform": "translateY(-2px)",
                            },
                        ),
                        spacing="4",
                        wrap="wrap",
                        align="center",
                        style={"gap": "1rem"},
                    ),
                    justify="between",
                    align="center",
                    direction=rx.breakpoints(initial="column", md="row"),
                    spacing="5",
                    width="100%",
                    style={
                        "gap": "2rem",
                        "paddingBottom": "2.5rem",
                        "borderBottom": f"1px solid {Color.BORDER.value}",
                    },
                ),
                # Bottom Copyright & Links Row
                rx.flex(
                    rx.text(
                        t(COPYRIGHT_ES, COPYRIGHT_EN),
                        font_family=Font.BODY.value,
                        color=TextColor.MUTED.value,
                        font_size="0.82rem",
                        font_weight="500",
                    ),
                    rx.hstack(
                        footer_social_link("GitHub", GITHUB_URL),
                        footer_social_link("Instagram", INSTAGRAM_URL),
                        spacing="4",
                        align="center",
                        style={"gap": "1rem"},
                    ),
                    justify="between",
                    align="center",
                    direction=rx.breakpoints(initial="column", sm="row"),
                    spacing="3",
                    width="100%",
                    style={"gap": "1rem", "paddingTop": "1.25rem"},
                ),
                width="100%",
                max_width=MAX_WIDTH,
                margin_x="auto",
                padding_x=["1.25rem", "2rem", "3rem"],
                padding_y=["3rem", "3.5rem"],
            ),
            width="100%",
            background=Color.BACKGROUND.value,
            border_top=f"2px solid {Color.ACCENT.value}",
        ),
        id="contact",
        style={"width": "100%"},
    )
