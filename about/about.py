import reflex as rx
from about.pages import index, publications
from about.styles import STYLESHEETS

app = rx.App()

# Add the stylesheet to the app
app.stylesheets.extend(STYLESHEETS)

# Define a global style
app.global_style = {
    "body": {
        "font_family": "Playfair Display, serif",  # Change to Playfair Display
        "margin": 0,
        "padding": 0,
    }
}