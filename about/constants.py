import reflex as rx
from datetime import datetime

# Social Media URLs
GITHUB_URL = "https://github.com/morabdiego"
LINKEDIN_URL = "https://www.linkedin.com/in/morabdiego/"
GMAIL_URL = "morabdiego@gmail.com"
INSTAGRAM_URL = "https://www.instagram.com/morabdiego/"
CV_URL = "https://drive.google.com/file/d/1h1djoliw5Gp4R2rFO0Ex4H8-WqHjdst-/view?usp=sharing"  # Spanish CV URL


# Social Links with icons and descriptions
SOCIAL_LINKS = [
    (CV_URL, "ico_cv.svg", "Descargar mi CV"),
    (f"mailto:{GMAIL_URL}", "ico_email.png", "Envíame un email a morabdiego@gmail.com"),
    (LINKEDIN_URL, "ico_linkedin.png", "Conéctate conmigo en LinkedIn"),
    (GITHUB_URL, "ico_github.png", "Mira mis proyectos"),
    (INSTAGRAM_URL, "ico_instagram.png", "Sígueme en Instagram")
]

# Layout
MAX_WIDTH = "1400px"
FORM_WIDTH = "600px"
FULL_WIDTH = "100%"

# Markdown paths - Spanish only now
ABOUT_MD = "assets/content/about-ES.md"
PUBLICATIONS_MD = "assets/content/publications-ES.md"
