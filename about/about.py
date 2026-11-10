import reflex as rx
from about.pages.index import index  # noqa: F401
from about.styles.styles import STYLESHEETS, GLOBAL_STYLE

app = rx.App(
    enable_state=False,
    stylesheets=STYLESHEETS,
    style=GLOBAL_STYLE,
)
