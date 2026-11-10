import reflex as rx
from reflex.experimental.client_state import ClientStateVar

# Client-side state variable for language switching (works 100% statically on GitHub Pages without a backend)
is_spanish = ClientStateVar.create("is_spanish", default=True)


def t(es_text: str, en_text: str) -> rx.Var:
    """Return reactive text based on current client-side language selection."""
    return rx.cond(is_spanish.value, es_text, en_text)
