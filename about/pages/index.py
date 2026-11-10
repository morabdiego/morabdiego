import reflex as rx
from about.components.navbar import navbar
from about.components.hero import hero
from about.components.cv_sections import (
    experience_section,
    education_section,
    skills_section,
    publications_section,
)
from about.components.footer import footer
from about.state import is_spanish


@rx.page(
    route="/",
    title="Diego Mora (@morabdiego) | Economista · Analista de Datos y Política Fiscal",
    description="Portfolio y CV de Diego J. Mora Benitez — Economista (UBA) especializado en econometría aplicada, analítica fiscal e investigación socioeconómica.",
)
def index() -> rx.Component:
    return rx.box(
        is_spanish,
        navbar(),
        rx.el.main(
            hero(),
            experience_section(),
            education_section(),
            skills_section(),
            publications_section(),
            style={"width": "100%"},
        ),
        footer(),
        width="100%",
        min_height="100vh",
    )
