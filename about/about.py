import reflex as rx
from about.pages.index import index
from about.pages.publications import publications
from about.api.api import hello
from about.styles.styles import STYLESHEETS

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

app.api.add_api_route("/hello", hello) # Add an API route test
