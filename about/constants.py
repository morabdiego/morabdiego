from datetime import datetime
from reflex_base.config import get_config


def asset_url(path: str) -> str:
    """Resolve an asset path taking into account frontend_path (e.g. /about on GitHub Pages)."""
    clean = "/" + path.lstrip("/")
    return get_config().prepend_frontend_path(clean)


# Social Media & Contact URLs
GITHUB_URL = "https://github.com/morabdiego"
OBSERVADATA_URL = "https://github.com/ObservatorioVillero/observadata"
OBSERVATORIO_WEB_URL = "https://observatoriovillero.lapoderosa.org.ar/"
LINKEDIN_URL = "https://www.linkedin.com/in/morabdiego/"
GMAIL_ADDRESS = "morabdiego@gmail.com"
GMAIL_URL = f"mailto:{GMAIL_ADDRESS}"
INSTAGRAM_URL = "https://www.instagram.com/morabdiego/"
CV_PDF_ES_PATH = "/content/CV-ES.pdf"
CV_PDF_EN_PATH = "/content/CV-EN.pdf"

# Page Information
AUTHOR = "Diego J. Mora Benitez"
HANDLE = "@morabdiego"
LOCATION_ES = "Ciudad de Buenos Aires, Argentina"
LOCATION_EN = "Buenos Aires, Argentina"
YEAR = str(datetime.now().year)
COPYRIGHT_EN = f"© {YEAR} {AUTHOR}. Built with Reflex."
COPYRIGHT_ES = f"© {YEAR} {AUTHOR}. Desarrollado con Reflex."

# One-Page Anchor Navigation (id, label_es, label_en)
NAV_SECTIONS = [
    ("#about", "Sobre mí", "About"),
    ("#experience", "Experiencia", "Experience"),
    ("#education", "Formación", "Education & Training"),
    ("#skills", "Habilidades", "Skills"),
    ("#publications", "Publicaciones", "Projects & Publications"),
]

# Social Links with icons and bilingual tooltips
SOCIAL_LINKS = [
    # (LINKEDIN_URL, "ico_linkedin.png", "LinkedIn", "Conectar en LinkedIn", "Connect on LinkedIn"),
    (GITHUB_URL, "ico_github.png", "GitHub", "Ver proyectos en GitHub", "Check out my GitHub"),
    (GMAIL_URL, "ico_email.png", "Email", f"Escribir a {GMAIL_ADDRESS}", f"Email me at {GMAIL_ADDRESS}"),
    (INSTAGRAM_URL, "ico_instagram.png", "Instagram", "Seguir en Instagram", "Follow on Instagram"),
]

# Layout dimensions
MAX_WIDTH = "1120px"
FULL_WIDTH = "100%"
