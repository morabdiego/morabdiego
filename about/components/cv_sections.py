import reflex as rx
from about.styles.styles import (
    Color,
    AltColor,
    AltTextColor,
    Font,
    CARD_STYLE,
)
from about.constants import MAX_WIDTH
from about.data import (
    EXPERIENCE,
    EDUCATION,
    TRAINING,
    SKILLS,
    PYPI_PACKAGES,
    PUBLICATIONS,
)
from about.state import (
    t,
    show_all_experience,
    show_all_training,
    show_all_publications,
)


def expandable_toggle_button(
    state_var,
    show_es: str,
    show_en: str,
    hide_es: str = "Mostrar menos",
    hide_en: str = "Show less",
) -> rx.Component:
    return rx.flex(
        rx.el.button(
            rx.hstack(
                rx.text(
                    rx.cond(
                        state_var.value,
                        t(hide_es, hide_en),
                        t(show_es, show_en),
                    ),
                    font_family=Font.BODY.value,
                    font_size="0.86rem",
                    font_weight="700",
                ),
                rx.cond(
                    state_var.value,
                    rx.icon("chevron-up", size=16),
                    rx.icon("chevron-down", size=16),
                ),
                spacing="2",
                align="center",
            ),
            type="button",
            on_click=state_var.set_value(rx.cond(state_var.value, False, True)),
            style={
                "display": "inline-flex",
                "align_items": "center",
                "padding": "0.7rem 1.4rem",
                "border_radius": "10px",
                "background": "rgba(251, 250, 243, 0.72)",
                "backdrop_filter": "blur(12px) saturate(140%)",
                "-webkit-backdrop-filter": "blur(12px) saturate(140%)",
                "color": AltTextColor.PRIMARY.value,
                "border": f"1px solid {AltColor.BORDER_STRONG.value}",
                "box_shadow": "inset 0 1px 0 rgba(255, 255, 255, 0.65), 0 4px 12px rgba(30, 30, 30, 0.04)",
                "cursor": "pointer",
                "transition": "all 0.2s ease",
            },
            _hover={
                "border_color": Color.ACCENT.value,
                "background": Color.ACCENT.value,
                "color": Color.BACKGROUND_DEEP.value,
                "transform": "translateY(-1px)",
            },
        ),
        justify="center",
        width="100%",
        style={"marginTop": "1.5rem"},
    )


def section_heading(
    kicker_es: str,
    kicker_en: str,
    title_es: str,
    title_en: str,
    subtitle_es: str = "",
    subtitle_en: str = "",
) -> rx.Component:
    return rx.vstack(
        rx.text(
            t(kicker_es, kicker_en),
            font_family=Font.BODY.value,
            font_size="0.76rem",
            font_weight="700",
            text_transform="uppercase",
            letter_spacing="0.12em",
            color=AltTextColor.UNEXPECTED.value,
        ),
        rx.heading(
            t(title_es, title_en),
            as_="h2",
            font_family=Font.HEADING.value,
            font_size=["1.8rem", "2.2rem", "2.5rem"],
            font_weight="700",
            color=AltTextColor.PRIMARY.value,
            line_height="1.15",
            letter_spacing="-0.025em",
        ),
        rx.cond(
            subtitle_es != "",
            rx.text(
                t(subtitle_es, subtitle_en),
                font_family=Font.BODY.value,
                font_size="0.95rem",
                font_weight="500",
                color=AltTextColor.MUTED.value,
                max_width="65ch",
                line_height="1.65",
            ),
        ),
        rx.box(
            width="48px",
            height="3px",
            background=Color.ACCENT.value,
            border_radius="999px",
            margin_top="0.4rem",
        ),
        spacing="2",
        align="start",
        width="100%",
        margin_bottom="2rem",
    )


def tag_pill(label_es: str, label_en: str = "", variant: str = "green") -> rx.Component:
    bg = (
        AltColor.ACCENT_SOFT.value
        if variant == "green"
        else AltColor.HIGHLIGHT_SOFT.value
    )
    fg = (
        AltTextColor.SECONDARY.value
        if variant == "green"
        else AltTextColor.UNEXPECTED.value
    )
    border_col = (
        "rgba(43, 122, 88, 0.22)"
        if variant == "green"
        else "rgba(155, 77, 77, 0.22)"
    )
    text_content = t(label_es, label_en) if label_en else label_es
    return rx.box(
        rx.text(
            text_content,
            font_family=Font.BODY.value,
            font_size="0.76rem",
            font_weight="600",
            color=fg,
        ),
        style={
            "display": "inline-flex",
            "align_items": "center",
            "padding": "0.32rem 0.8rem",
            "border_radius": "999px",
            "background": bg,
            "border": f"1px solid {border_col}",
        },
    )


def bullet_row(es_text: str, en_text: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            width="7px",
            height="7px",
            border_radius="50%",
            background=Color.ACCENT.value,
            margin_top="0.55rem",
            flex_shrink="0",
        ),
        rx.text(
            t(es_text, en_text),
            font_family=Font.BODY.value,
            font_size="0.93rem",
            font_weight="400",
            color=AltTextColor.PRIMARY.value,
            line_height="1.68",
            max_width="68ch",
        ),
        spacing="3",
        align="start",
        width="100%",
    )


def experience_card(item: dict) -> rx.Component:
    bullets = list(zip(item["bullets_es"], item["bullets_en"]))
    tags = list(zip(item["tags_es"], item["tags_en"]))
    card_css = {
        **CARD_STYLE,
        "border_left": (
            f"4px solid {Color.ACCENT.value}"
            if item["current"]
            else f"4px solid {AltColor.BORDER_STRONG.value}"
        ),
    }
    return rx.box(
        rx.vstack(
            # Header row: Icon + Role + Organization + Period badge
            rx.flex(
                rx.hstack(
                    rx.box(
                        rx.icon(
                            item["icon"],
                            size=22,
                            color=AltTextColor.SECONDARY.value,
                        ),
                        style={
                            "display": "inline-flex",
                            "align_items": "center",
                            "justify_content": "center",
                            "width": "46px",
                            "height": "46px",
                            "border_radius": "12px",
                            "background": AltColor.ACCENT_SOFT.value,
                            "flex_shrink": "0",
                        },
                    ),
                    rx.vstack(
                        rx.flex(
                            rx.heading(
                                t(item["role_es"], item["role_en"]),
                                as_="h3",
                                font_family=Font.HEADING.value,
                                font_size=["1.12rem", "1.25rem"],
                                font_weight="700",
                                color=AltTextColor.PRIMARY.value,
                                letter_spacing="-0.02em",
                            ),
                            rx.cond(
                                item["current"],
                                rx.box(
                                    rx.text(
                                        t("ACTUAL", "CURRENT"),
                                        font_family=Font.BODY.value,
                                        font_size="0.68rem",
                                        font_weight="800",
                                        letter_spacing="0.06em",
                                        color=Color.BACKGROUND_DEEP.value,
                                    ),
                                    style={
                                        "display": "inline-flex",
                                        "align_items": "center",
                                        "padding": "0.2rem 0.65rem",
                                        "border_radius": "999px",
                                        "background": Color.ACCENT.value,
                                    },
                                ),
                            ),
                            spacing="3",
                            align="center",
                            wrap="wrap",
                            style={"gap": "0.65rem"},
                        ),
                        rx.flex(
                            rx.text(
                                t(item["organization_es"], item["organization_en"]),
                                font_family=Font.BODY.value,
                                font_weight="700",
                                font_size="0.92rem",
                                color=AltTextColor.UNEXPECTED.value,
                            ),
                            rx.text("·", color=AltTextColor.MUTED.value),
                            rx.text(
                                t(item["location_es"], item["location_en"]),
                                font_family=Font.BODY.value,
                                font_size="0.86rem",
                                font_weight="500",
                                color=AltTextColor.MUTED.value,
                            ),
                            spacing="2",
                            wrap="wrap",
                            align="center",
                            style={"gap": "0.45rem"},
                        ),
                        spacing="1",
                        align="start",
                    ),
                    spacing="3",
                    align="start",
                    flex="1",
                    min_width="0",
                    style={"gap": "1rem"},
                ),
                rx.hstack(
                    rx.icon("calendar", size=14, color=AltTextColor.MUTED.value),
                    rx.text(
                        t(item["period_es"], item["period_en"]),
                        font_family=Font.BODY.value,
                        font_size="0.78rem",
                        font_weight="600",
                        color=AltTextColor.MUTED.value,
                        white_space="nowrap",
                    ),
                    spacing="2",
                    align="center",
                    style={
                        "display": "inline-flex",
                        "align_items": "center",
                        "padding": "0.38rem 0.85rem",
                        "border_radius": "999px",
                        "background": AltColor.BACKGROUND.value,
                        "border": f"1px solid {AltColor.BORDER_STRONG.value}",
                        "flex_shrink": "0",
                    },
                ),
                justify="between",
                align="start",
                direction=rx.breakpoints(initial="column", md="row"),
                spacing="3",
                width="100%",
                style={"gap": "1rem"},
            ),
            # Responsibilities list
            rx.vstack(
                *[bullet_row(es, en) for es, en in bullets],
                spacing="2",
                width="100%",
                style={"gap": "0.55rem", "paddingTop": "0.4rem"},
            ),
            # Tags
            rx.flex(
                *[tag_pill(es, en, "green") for es, en in tags],
                spacing="2",
                wrap="wrap",
                style={"gap": "0.55rem", "paddingTop": "0.4rem"},
            ),
            spacing="4",
            align="start",
            width="100%",
        ),
        style=card_css,
        width="100%",
    )


def experience_section() -> rx.Component:
    return rx.el.section(
        rx.box(
            section_heading(
                "Trayectoria Profesional",
                "Career Path",
                "Experiencia Profesional",
                "Professional Experience",
                "Econometría aplicada, estimación de recaudación e inteligencia fiscal en ARBA, dirección de investigaciones federales en el Observatorio Villero y divulgación económica.",
                "Applied econometrics, revenue forecasting and fiscal intelligence at ARBA, nationwide research leadership at the Socioeconomic Observatory, and economic outreach.",
            ),
            rx.vstack(
                *[experience_card(item) for item in EXPERIENCE[:2]],
                rx.box(
                    experience_card(EXPERIENCE[2]),
                    rx.cond(
                        ~show_all_experience.value,
                        rx.box(
                            style={
                                "position": "absolute",
                                "bottom": "0",
                                "left": "0",
                                "right": "0",
                                "height": "95px",
                                "pointer_events": "none",
                                "background": f"linear-gradient(to bottom, rgba(230, 227, 205, 0) 0%, {AltColor.BACKGROUND_ALT.value} 92%)",
                            }
                        ),
                    ),
                    position="relative",
                    width="100%",
                    max_height=rx.cond(show_all_experience.value, "none", "130px"),
                    overflow=rx.cond(show_all_experience.value, "visible", "hidden"),
                ),
                rx.cond(
                    show_all_experience.value,
                    rx.vstack(
                        *[experience_card(item) for item in EXPERIENCE[3:]],
                        spacing="5",
                        width="100%",
                        style={"gap": "1.5rem"},
                    ),
                ),
                spacing="5",
                width="100%",
                style={"gap": "1.5rem"},
            ),
            expandable_toggle_button(
                show_all_experience,
                f"Ver toda la experiencia ({len(EXPERIENCE)})",
                f"Show all experience ({len(EXPERIENCE)})",
            ),
            width="100%",
            max_width=MAX_WIDTH,
            margin_x="auto",
            padding_x=["1.25rem", "2rem", "3rem"],
            padding_y=["3.75rem", "4.75rem"],
        ),
        id="experience",
        style={
            "width": "100%",
            "background": AltColor.BACKGROUND_ALT.value,
            "border_top": f"1px solid {AltColor.BORDER.value}",
            "border_bottom": f"1px solid {AltColor.BORDER.value}",
        },
    )


def education_degree_card(item: dict) -> rx.Component:
    card_css = {
        **CARD_STYLE,
        "border_left": f"4px solid {AltTextColor.UNEXPECTED.value}",
    }
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.hstack(
                    rx.box(
                        rx.icon(
                            "graduation-cap",
                            size=24,
                            color=AltTextColor.UNEXPECTED.value,
                        ),
                        style={
                            "display": "inline-flex",
                            "align_items": "center",
                            "justify_content": "center",
                            "width": "48px",
                            "height": "48px",
                            "border_radius": "12px",
                            "background": AltColor.HIGHLIGHT_SOFT.value,
                            "flex_shrink": "0",
                        },
                    ),
                    rx.vstack(
                        rx.text(
                            t(item["badge_es"], item["badge_en"]),
                            font_family=Font.BODY.value,
                            font_size="0.72rem",
                            font_weight="700",
                            text_transform="uppercase",
                            letter_spacing="0.08em",
                            color=AltTextColor.UNEXPECTED.value,
                        ),
                        rx.heading(
                            t(item["degree_es"], item["degree_en"]),
                            as_="h3",
                            font_family=Font.HEADING.value,
                            font_size=["1.2rem", "1.4rem"],
                            font_weight="800",
                            color=AltTextColor.PRIMARY.value,
                            letter_spacing="-0.02em",
                        ),
                        rx.flex(
                            rx.text(
                                item["institution"],
                                font_family=Font.BODY.value,
                                font_weight="700",
                                font_size="0.94rem",
                                color=AltTextColor.SECONDARY.value,
                            ),
                            rx.text("·", color=AltTextColor.MUTED.value),
                            rx.text(
                                t(item["faculty_es"], item["faculty_en"]),
                                font_family=Font.BODY.value,
                                font_weight="500",
                                font_size="0.9rem",
                                color=AltTextColor.MUTED.value,
                            ),
                            spacing="2",
                            wrap="wrap",
                            align="center",
                            style={"gap": "0.45rem"},
                        ),
                        spacing="1",
                        align="start",
                    ),
                    spacing="3",
                    align="start",
                    flex="1",
                    min_width="0",
                    style={"gap": "1rem"},
                ),
                rx.hstack(
                    rx.icon("calendar", size=14, color=AltTextColor.MUTED.value),
                    rx.text(
                        t(item["date_es"], item["date_en"]),
                        font_family=Font.BODY.value,
                        font_size="0.78rem",
                        font_weight="600",
                        color=AltTextColor.MUTED.value,
                        white_space="nowrap",
                    ),
                    spacing="2",
                    align="center",
                    style={
                        "display": "inline-flex",
                        "align_items": "center",
                        "padding": "0.38rem 0.85rem",
                        "border_radius": "999px",
                        "background": AltColor.BACKGROUND.value,
                        "border": f"1px solid {AltColor.BORDER_STRONG.value}",
                        "flex_shrink": "0",
                    },
                ),
                justify="between",
                align="start",
                direction=rx.breakpoints(initial="column", md="row"),
                spacing="3",
                width="100%",
                style={"gap": "1rem"},
            ),
            rx.text(
                t(item["description_es"], item["description_en"]),
                font_family=Font.BODY.value,
                font_size="0.94rem",
                font_weight="400",
                color=AltTextColor.MUTED.value,
                line_height="1.65",
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        style=card_css,
        width="100%",
    )


def training_card(item: dict) -> rx.Component:
    tags = list(zip(item["tags_es"], item["tags_en"]))
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    item["institution"],
                    font_family=Font.BODY.value,
                    font_weight="700",
                    font_size="0.82rem",
                    text_transform="uppercase",
                    letter_spacing="0.06em",
                    color=AltTextColor.UNEXPECTED.value,
                ),
                rx.text(
                    t(item["date_es"], item["date_en"]),
                    font_family=Font.MONO.value,
                    font_size="0.76rem",
                    font_weight="600",
                    color=AltTextColor.MUTED.value,
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            rx.heading(
                t(item["title_es"], item["title_en"]),
                as_="h4",
                font_family=Font.HEADING.value,
                font_size="1.12rem",
                font_weight="700",
                color=AltTextColor.PRIMARY.value,
                line_height="1.35",
                letter_spacing="-0.015em",
            ),
            rx.text(
                t(item["description_es"], item["description_en"]),
                font_family=Font.BODY.value,
                font_size="0.89rem",
                font_weight="400",
                color=AltTextColor.MUTED.value,
                line_height="1.65",
                flex="1",
            ),
            rx.flex(
                *[tag_pill(es, en, "green") for es, en in tags],
                spacing="2",
                wrap="wrap",
                style={"gap": "0.5rem", "paddingTop": "0.35rem"},
            ),
            spacing="3",
            align="start",
            width="100%",
            height="100%",
        ),
        style={
            "background": "rgba(251, 250, 243, 0.72)",
            "backdrop_filter": "blur(14px) saturate(140%)",
            "-webkit-backdrop-filter": "blur(14px) saturate(140%)",
            "border": f"1px solid {AltColor.BORDER_STRONG.value}",
            "border_top": f"2px solid {Color.ACCENT.value}",
            "border_radius": "10px",
            "padding": ["1.25rem", "1.5rem"],
            "box_shadow": "inset 0 1px 0 rgba(255, 255, 255, 0.65), 0 4px 16px -4px rgba(30, 30, 30, 0.05)",
            "transition": "background 0.2s ease, border-color 0.2s ease",
            "_hover": {
                "background": "rgba(251, 250, 243, 0.88)",
                "border_color": Color.ACCENT.value,
            },
        },
        width="100%",
        height="100%",
    )


def education_section() -> rx.Component:
    return rx.el.section(
        rx.box(
            section_heading(
                "Formación Académica",
                "Academic Background",
                "Educación y Formación Continua",
                "Education & Continuous Training",
                "Formación universitaria de grado en Economía (UBA), Diplomatura en Análisis de Datos para el Sector Público (IPAP – UTN La Plata) y especialización continua.",
                "University degree in Economics (UBA), Diploma in Data Analysis for the Public Sector (IPAP – UTN La Plata), and continuous specialization.",
            ),
            rx.vstack(
                # Grado Universitario y Diplomatura
                *[education_degree_card(item) for item in EDUCATION],
                # Subheader for Formación Continua / Especialización
                rx.hstack(
                    rx.icon("sparkles", size=19, color=AltTextColor.SECONDARY.value),
                    rx.text(
                        t(
                            "Cursos de Especialización y Formación Continua",
                            "Additional Training & Specialization Courses",
                        ),
                        font_family=Font.HEADING.value,
                        font_size="1.15rem",
                        font_weight="700",
                        color=AltTextColor.PRIMARY.value,
                        letter_spacing="-0.01em",
                    ),
                    spacing="2",
                    align="center",
                    style={"paddingTop": "1.25rem", "paddingBottom": "0.25rem"},
                ),
                rx.grid(
                    *[training_card(item) for item in TRAINING[:2]],
                    columns=rx.breakpoints(initial="1", md="2"),
                    spacing="5",
                    width="100%",
                    style={"gap": "1.5rem"},
                ),
                rx.box(
                    rx.grid(
                        *[training_card(item) for item in TRAINING[2:]],
                        columns=rx.breakpoints(initial="1", md="2"),
                        spacing="5",
                        width="100%",
                        style={"gap": "1.5rem"},
                    ),
                    rx.cond(
                        ~show_all_training.value,
                        rx.box(
                            style={
                                "position": "absolute",
                                "bottom": "0",
                                "left": "0",
                                "right": "0",
                                "height": "90px",
                                "pointer_events": "none",
                                "background": f"linear-gradient(to bottom, rgba(240, 238, 220, 0) 0%, {AltColor.BACKGROUND.value} 92%)",
                            }
                        ),
                    ),
                    position="relative",
                    width="100%",
                    max_height=rx.cond(show_all_training.value, "none", "125px"),
                    overflow=rx.cond(show_all_training.value, "visible", "hidden"),
                ),
                expandable_toggle_button(
                    show_all_training,
                    f"Ver todos los cursos ({len(TRAINING)})",
                    f"Show all courses ({len(TRAINING)})",
                ),
                spacing="4",
                align="start",
                width="100%",
                style={"gap": "1.25rem"},
            ),
            width="100%",
            max_width=MAX_WIDTH,
            margin_x="auto",
            padding_x=["1.25rem", "2rem", "3rem"],
            padding_y=["3.75rem", "4.75rem"],
        ),
        id="education",
        style={
            "width": "100%",
            "background": AltColor.BACKGROUND.value,
        },
    )


def skill_category_card(item: dict) -> rx.Component:
    skills = list(zip(item["items_es"], item["items_en"]))
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.icon(
                    item["icon"],
                    size=18,
                    color=AltTextColor.SECONDARY.value,
                ),
                rx.heading(
                    t(item["category_es"], item["category_en"]),
                    as_="h3",
                    font_family=Font.HEADING.value,
                    font_size="1.14rem",
                    font_weight="700",
                    color=AltTextColor.PRIMARY.value,
                    letter_spacing="-0.015em",
                ),
                spacing="2",
                align="center",
            ),
            rx.text(
                t(item["description_es"], item["description_en"]),
                font_family=Font.BODY.value,
                font_size="0.88rem",
                font_weight="400",
                color=AltTextColor.MUTED.value,
                line_height="1.6",
            ),
            rx.flex(
                *[
                    rx.box(
                        rx.text(
                            t(es, en),
                            font_family=Font.BODY.value,
                            font_size="0.79rem",
                            font_weight="600",
                            color=AltTextColor.PRIMARY.value,
                        ),
                        style={
                            "display": "inline-flex",
                            "align_items": "center",
                            "padding": "0.34rem 0.72rem",
                            "border_radius": "8px",
                            "background": AltColor.CARD_BG.value,
                            "border": f"1px solid {AltColor.BORDER_STRONG.value}",
                        },
                    )
                    for es, en in skills
                ],
                spacing="2",
                wrap="wrap",
                style={"gap": "0.5rem", "paddingTop": "0.25rem"},
            ),
            spacing="3",
            align="start",
            width="100%",
            height="100%",
        ),
        style={
            "padding_top": "1.25rem",
            "border_top": f"2px solid {AltColor.BORDER_STRONG.value}",
        },
        width="100%",
        height="100%",
    )


def skills_section() -> rx.Component:
    return rx.el.section(
        rx.box(
            section_heading(
                "Capacidades Técnicas",
                "Technical Capabilities",
                "Habilidades y Herramientas",
                "Skills & Toolkit",
                "Dominio del ciclo completo del dato: econometría aplicada, ingeniería de datos (ETL y APIs), operativos estadísticos en campo, visualización y ciencia abierta.",
                "Full-cycle data capabilities: applied econometrics, data engineering (ETL & APIs), field survey operations, visualization, and open science.",
            ),
            rx.grid(
                *[skill_category_card(item) for item in SKILLS],
                columns=rx.breakpoints(initial="1", md="3"),
                spacing="5",
                width="100%",
                style={"gap": "1.5rem"},
            ),
            width="100%",
            max_width=MAX_WIDTH,
            margin_x="auto",
            padding_x=["1.25rem", "2rem", "3rem"],
            padding_y=["3.75rem", "4.75rem"],
        ),
        id="skills",
        style={
            "width": "100%",
            "background": AltColor.BACKGROUND_ALT.value,
            "border_top": f"1px solid {AltColor.BORDER.value}",
            "border_bottom": f"1px solid {AltColor.BORDER.value}",
        },
    )


def publication_link_button(link: dict, idx: int = 0) -> rx.Component:
    is_primary = idx == 0
    return rx.el.a(
        rx.hstack(
            rx.text(
                t(link["label_es"], link["label_en"]),
                font_family=Font.BODY.value,
                font_size="0.8rem",
                font_weight="700",
            ),
            rx.icon("arrow-up-right", size=14),
            spacing="1",
            align="center",
        ),
        href=link["url"],
        target="_blank",
        rel="noopener noreferrer",
        style={
            "display": "inline-flex",
            "align_items": "center",
            "padding": "0.42rem 0.9rem",
            "border_radius": "999px",
            "background": (
                AltColor.ACCENT_SOFT.value
                if is_primary
                else AltColor.BACKGROUND.value
            ),
            "color": (
                AltTextColor.SECONDARY.value
                if is_primary
                else AltTextColor.PRIMARY.value
            ),
            "border": (
                "1px solid rgba(43, 122, 88, 0.25)"
                if is_primary
                else f"1px solid {AltColor.BORDER_STRONG.value}"
            ),
            "text_decoration": "none",
            "transition": "all 0.2s ease",
        },
        _hover={
            "background": Color.ACCENT.value,
            "color": Color.BACKGROUND_DEEP.value,
            "border_color": Color.ACCENT.value,
            "transform": "translateY(-1px)",
        },
    )


def publication_card(item: dict) -> rx.Component:
    is_green = item["accent"] == "green"
    links = item.get("links", [])
    has_description = bool(item.get("description_es"))
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        item["icon"],
                        size=15,
                        color=(
                            AltTextColor.SECONDARY.value
                            if is_green
                            else AltTextColor.UNEXPECTED.value
                        ),
                    ),
                    rx.text(
                        t(item["type_es"], item["type_en"]),
                        font_family=Font.BODY.value,
                        font_size="0.72rem",
                        font_weight="700",
                        text_transform="uppercase",
                        letter_spacing="0.06em",
                        color=(
                            AltTextColor.SECONDARY.value
                            if is_green
                            else AltTextColor.UNEXPECTED.value
                        ),
                    ),
                    spacing="2",
                    align="center",
                    style={
                        "display": "inline-flex",
                        "align_items": "center",
                        "padding": "0.3rem 0.75rem",
                        "border_radius": "999px",
                        "background": (
                            AltColor.ACCENT_SOFT.value
                            if is_green
                            else AltColor.HIGHLIGHT_SOFT.value
                        ),
                    },
                ),
                rx.text(
                    item["year"],
                    font_family=Font.BODY.value,
                    font_size="0.78rem",
                    font_weight="700",
                    color=AltTextColor.MUTED.value,
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            rx.heading(
                t(item["title_es"], item["title_en"]),
                as_="h3",
                font_family=Font.HEADING.value,
                font_size=["1.05rem", "1.14rem"],
                font_weight="700",
                color=AltTextColor.PRIMARY.value,
                line_height="1.45",
                letter_spacing="-0.01em",
            ),
            rx.text(
                item["authors"],
                font_family=Font.BODY.value,
                font_size="0.86rem",
                font_weight="600",
                color=AltTextColor.PRIMARY.value,
            ),
            rx.cond(
                has_description,
                rx.text(
                    t(item.get("description_es", ""), item.get("description_en", "")),
                    font_family=Font.BODY.value,
                    font_size="0.88rem",
                    font_weight="400",
                    color=AltTextColor.MUTED.value,
                    line_height="1.62",
                ),
            ),
            rx.text(
                t(item["venue_es"], item["venue_en"]),
                font_family=Font.BODY.value,
                font_size="0.82rem",
                font_style="italic",
                font_weight="500",
                color=AltTextColor.MUTED.value,
                line_height="1.5",
            ),
            rx.cond(
                len(links) > 0,
                rx.flex(
                    *[
                        publication_link_button(link, idx)
                        for idx, link in enumerate(links)
                    ],
                    spacing="2",
                    wrap="wrap",
                    style={"gap": "0.55rem", "paddingTop": "0.35rem"},
                ),
            ),
            spacing="3",
            align="start",
            width="100%",
            height="100%",
        ),
        style=CARD_STYLE,
        width="100%",
        height="100%",
    )


def publication_list_row(item: dict) -> rx.Component:
    is_green = item["accent"] == "green"
    links = item.get("links", [])
    has_description = bool(item.get("description_es"))
    return rx.box(
        rx.flex(
            # Left metadata column
            rx.vstack(
                rx.text(
                    item["year"],
                    font_family=Font.MONO.value,
                    font_size="0.8rem",
                    font_weight="600",
                    color=AltTextColor.PRIMARY.value,
                ),
                rx.text(
                    t(item["type_es"], item["type_en"]),
                    font_family=Font.BODY.value,
                    font_size="0.72rem",
                    font_weight="700",
                    text_transform="uppercase",
                    letter_spacing="0.06em",
                    color=(
                        AltTextColor.SECONDARY.value
                        if is_green
                        else AltTextColor.UNEXPECTED.value
                    ),
                ),
                spacing="1",
                align="start",
                width=["100%", "100%", "210px"],
                flex_shrink="0",
            ),
            # Right editorial content column
            rx.vstack(
                rx.heading(
                    t(item["title_es"], item["title_en"]),
                    as_="h3",
                    font_family=Font.HEADING.value,
                    font_size=["1.05rem", "1.15rem"],
                    font_weight="700",
                    color=AltTextColor.PRIMARY.value,
                    line_height="1.38",
                    letter_spacing="-0.015em",
                ),
                rx.text(
                    item["authors"],
                    font_family=Font.BODY.value,
                    font_size="0.84rem",
                    font_weight="600",
                    color=AltTextColor.PRIMARY.value,
                ),
                rx.cond(
                    has_description,
                    rx.text(
                        t(
                            item.get("description_es", ""),
                            item.get("description_en", ""),
                        ),
                        font_family=Font.BODY.value,
                        font_size="0.88rem",
                        font_weight="400",
                        color=AltTextColor.MUTED.value,
                        line_height="1.65",
                        max_width="65ch",
                    ),
                ),
                rx.text(
                    t(item["venue_es"], item["venue_en"]),
                    font_family=Font.BODY.value,
                    font_size="0.8rem",
                    font_style="italic",
                    font_weight="500",
                    color=AltTextColor.MUTED.value,
                ),
                rx.cond(
                    len(links) > 0,
                    rx.flex(
                        *[
                            publication_link_button(link, idx)
                            for idx, link in enumerate(links)
                        ],
                        spacing="2",
                        wrap="wrap",
                        style={"gap": "0.55rem", "paddingTop": "0.35rem"},
                    ),
                ),
                spacing="2",
                align="start",
                width="100%",
                flex="1",
                min_width="0",
            ),
            direction=rx.breakpoints(initial="column", md="row"),
            align="start",
            width="100%",
            style={"gap": "1.25rem"},
        ),
        style={
            "padding_y": "1.6rem",
            "border_top": f"1px solid {AltColor.BORDER_STRONG.value}",
        },
        width="100%",
    )


def pypi_package_card(item: dict) -> rx.Component:
    links = [
        {
            "label_es": "Ver en PyPI",
            "label_en": "View on PyPI",
            "url": item["pypi_url"],
        },
        {
            "label_es": "GitHub",
            "label_en": "GitHub",
            "url": item["github_url"],
        },
    ]
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        item["icon"],
                        size=15,
                        color=AltTextColor.SECONDARY.value,
                    ),
                    rx.text(
                        t(item["category_es"], item["category_en"]),
                        font_family=Font.BODY.value,
                        font_size="0.72rem",
                        font_weight="700",
                        text_transform="uppercase",
                        letter_spacing="0.06em",
                        color=AltTextColor.SECONDARY.value,
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    "PyPI",
                    font_family=Font.MONO.value,
                    font_size="0.72rem",
                    font_weight="600",
                    color=AltTextColor.UNEXPECTED.value,
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            rx.flex(
                rx.heading(
                    item["name"],
                    as_="h3",
                    font_family=Font.HEADING.value,
                    font_size=["1.18rem", "1.28rem"],
                    font_weight="700",
                    color=AltTextColor.PRIMARY.value,
                    letter_spacing="-0.02em",
                ),
                rx.box(
                    rx.hstack(
                        rx.icon("terminal", size=13, color=Color.ACCENT.value),
                        rx.text(
                            item["install_cmd"],
                            font_family=Font.MONO.value,
                            font_size="0.74rem",
                            font_weight="600",
                            color=Color.PRIMARY.value,
                        ),
                        spacing="2",
                        align="center",
                    ),
                    style={
                        "display": "inline-flex",
                        "align_items": "center",
                        "padding": "0.26rem 0.65rem",
                        "border_radius": "8px",
                        "background": Color.BACKGROUND.value,
                    },
                ),
                justify="between",
                align="center",
                wrap="wrap",
                width="100%",
                style={"gap": "0.6rem"},
            ),
            rx.text(
                t(item["description_es"], item["description_en"]),
                font_family=Font.BODY.value,
                font_size="0.88rem",
                font_weight="400",
                color=AltTextColor.MUTED.value,
                line_height="1.62",
                flex="1",
            ),
            rx.flex(
                *[
                    publication_link_button(link, idx)
                    for idx, link in enumerate(links)
                ],
                spacing="2",
                wrap="wrap",
                style={"gap": "0.55rem", "paddingTop": "0.2rem"},
            ),
            spacing="3",
            align="start",
            width="100%",
            height="100%",
        ),
        style={
            "padding_top": "1.25rem",
            "padding_bottom": "0.5rem",
            "border_top": f"2px solid {Color.ACCENT.value}",
        },
        width="100%",
        height="100%",
    )


def publications_section() -> rx.Component:
    return rx.el.section(
        rx.box(
            section_heading(
                "Relevamientos, Producción Académica y Software Open-Source",
                "Surveys, Academic Output & Open-Source Software",
                "Proyectos, Publicaciones y Librerías",
                "Projects, Publications & Packages",
                "Plataformas interactivas de análisis, relevamientos socioeconómicos federales, ciencia abierta (Observadata) y librerías de Python publicadas en PyPI.",
                "Interactive analytics platforms, nationwide socioeconomic surveys, open science (Observadata), and Python libraries published on PyPI.",
            ),
            # Subheader 1: Investigaciones, Relevamientos y Publicaciones
            rx.flex(
                rx.hstack(
                    rx.icon("book-open", size=20, color=AltTextColor.SECONDARY.value),
                    rx.text(
                        t(
                            "Investigaciones, Relevamientos y Plataformas Interactivas",
                            "Research, Surveys & Interactive Platforms",
                        ),
                        font_family=Font.HEADING.value,
                        font_size="1.2rem",
                        font_weight="800",
                        color=AltTextColor.PRIMARY.value,
                        letter_spacing="-0.02em",
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.flex(
                    rx.el.a(
                        rx.hstack(
                            rx.icon("globe", size=16),
                            rx.text(
                                t(
                                    "Sitio oficial del Observatorio Villero",
                                    "Observatorio Villero Official Website",
                                ),
                                font_family=Font.BODY.value,
                                font_size="0.82rem",
                                font_weight="700",
                            ),
                            rx.icon("arrow-up-right", size=15),
                            spacing="2",
                            align="center",
                        ),
                        href="https://observatoriovillero.lapoderosa.org.ar/",
                        target="_blank",
                        rel="noopener noreferrer",
                        style={
                            "display": "inline-flex",
                            "align_items": "center",
                            "padding": "0.5rem 1rem",
                            "border_radius": "999px",
                            "background": Color.BACKGROUND.value,
                            "color": Color.PRIMARY.value,
                            "text_decoration": "none",
                            "transition": "all 0.2s ease",
                        },
                        _hover={
                            "background": Color.ACCENT.value,
                            "color": Color.BACKGROUND_DEEP.value,
                            "transform": "translateY(-1px)",
                        },
                    ),
                    rx.el.a(
                        rx.hstack(
                            rx.icon("database", size=16),
                            rx.text(
                                t(
                                    "Observadata · Datos Abiertos (GitHub)",
                                    "Observadata · Open Data (GitHub)",
                                ),
                                font_family=Font.BODY.value,
                                font_size="0.82rem",
                                font_weight="700",
                            ),
                            rx.icon("arrow-up-right", size=15),
                            spacing="2",
                            align="center",
                        ),
                        href="https://github.com/ObservatorioVillero/observadata",
                        target="_blank",
                        rel="noopener noreferrer",
                        style={
                            "display": "inline-flex",
                            "align_items": "center",
                            "padding": "0.5rem 1rem",
                            "border_radius": "999px",
                            "background": AltColor.ACCENT_SOFT.value,
                            "color": AltTextColor.SECONDARY.value,
                            "border": "1px solid rgba(43, 122, 88, 0.25)",
                            "text_decoration": "none",
                            "transition": "all 0.2s ease",
                        },
                        _hover={
                            "background": Color.ACCENT.value,
                            "color": Color.BACKGROUND_DEEP.value,
                            "transform": "translateY(-1px)",
                        },
                    ),
                    spacing="3",
                    wrap="wrap",
                    align="center",
                    style={"gap": "0.65rem"},
                ),
                justify="between",
                align="center",
                direction=rx.breakpoints(initial="column", md="row"),
                wrap="wrap",
                width="100%",
                style={"gap": "1rem", "marginBottom": "1.25rem"},
            ),
            # Uniform Editorial Archive List: first 3 + half of 4th with fade + expand toggle
            rx.vstack(
                *[publication_list_row(item) for item in PUBLICATIONS[:3]],
                rx.box(
                    publication_list_row(PUBLICATIONS[3]),
                    rx.cond(
                        ~show_all_publications.value,
                        rx.box(
                            style={
                                "position": "absolute",
                                "bottom": "0",
                                "left": "0",
                                "right": "0",
                                "height": "90px",
                                "pointer_events": "none",
                                "background": f"linear-gradient(to bottom, rgba(240, 238, 220, 0) 0%, {AltColor.BACKGROUND.value} 92%)",
                            }
                        ),
                    ),
                    position="relative",
                    width="100%",
                    max_height=rx.cond(show_all_publications.value, "none", "130px"),
                    overflow=rx.cond(show_all_publications.value, "visible", "hidden"),
                ),
                rx.cond(
                    show_all_publications.value,
                    rx.vstack(
                        *[publication_list_row(item) for item in PUBLICATIONS[4:]],
                        spacing="0",
                        width="100%",
                    ),
                ),
                spacing="0",
                width="100%",
                style={
                    "border_bottom": f"1px solid {AltColor.BORDER_STRONG.value}",
                },
            ),
            expandable_toggle_button(
                show_all_publications,
                f"Ver todas las investigaciones ({len(PUBLICATIONS)})",
                f"Show all publications ({len(PUBLICATIONS)})",
            ),
            # Subheader 2: Librerías Open-Source en PyPI
            rx.hstack(
                rx.icon("package", size=20, color=AltTextColor.SECONDARY.value),
                rx.text(
                    t(
                        "Librerías Open-Source en Python (PyPI)",
                        "Open-Source Python Packages (PyPI)",
                    ),
                    font_family=Font.HEADING.value,
                    font_size="1.2rem",
                    font_weight="800",
                    color=AltTextColor.PRIMARY.value,
                    letter_spacing="-0.02em",
                ),
                spacing="2",
                align="center",
                style={"marginTop": "3.25rem", "marginBottom": "1rem"},
            ),
            rx.grid(
                *[pypi_package_card(item) for item in PYPI_PACKAGES],
                columns=rx.breakpoints(initial="1", md="2"),
                spacing="5",
                width="100%",
                style={"gap": "1.5rem"},
            ),
            width="100%",
            max_width=MAX_WIDTH,
            margin_x="auto",
            padding_x=["1.25rem", "2rem", "3rem"],
            padding_y=["3.75rem", "4.75rem"],
        ),
        id="publications",
        style={
            "width": "100%",
            "background": AltColor.BACKGROUND.value,
        },
    )
