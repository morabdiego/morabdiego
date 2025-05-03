import reflex as rx
from datetime import datetime

# Social Media URLs
GITHUB_URL = "https://github.com/morabdiego"
LINKEDIN_URL = "https://www.linkedin.com/in/morabdiego/"
GMAIL_URL = "morabdiego@gmail.com"
INSTAGRAM_URL = "https://www.instagram.com/morabdiego/"
CV_URL = "https://drive.google.com/file/d/1lwOTeUCNgI_H3bU7rwT6sjUkp0IwfIqo/view?usp=sharing"

# Page Information
AUTHOR = "Diego Mora"
YEAR = str(datetime.now().year)
COPYRIGHT_EN = f"Copyright © {YEAR}. Created by {AUTHOR}"
COPYRIGHT_ES = f"Copyright © {YEAR}. Creado por {AUTHOR}"

# Navigation
NAV_LINKS_EN = [
    ["Home", "/"],
    ["Publications", "/publications"],
]

NAV_LINKS_ES = [
    ["Inicio", "/"],
    ["Publicaciones", "/publications"],
]

# Social Links with icons and descriptions
SOCIAL_LINKS = [
    (CV_URL, "ico_cv.svg", "Download my CV"),
    (f"mailto:{GMAIL_URL}", "ico_email.png", "Email me at morabdiego@gmail.com"),
    (LINKEDIN_URL, "ico_linkedin.png", "Connect with me on LinkedIn"),
    (GITHUB_URL, "ico_github.png", "Check out my projects"),
    (INSTAGRAM_URL, "ico_instagram.png", "Follow me on Instagram")
]

# Layout
MAX_WIDTH = "1400px"
FORM_WIDTH = "600px"
FULL_WIDTH = "100%"

# Markdown paths
ABOUT_MD_EN = "assets/content/about-EN.md"
ABOUT_MD_ES = "assets/content/about-ES.md"
PUBLICATIONS_MD_EN = "assets/content/publications-EN.md"
PUBLICATIONS_MD_ES = "assets/content/publications-ES.md"
