import reflex as rx
from reflex.experimental.client_state import ClientStateVar

# Client-side state variables (work 100% statically on GitHub Pages without a backend)
is_spanish = ClientStateVar.create("is_spanish", default=True)
mobile_menu_open = ClientStateVar.create("mobile_menu_open", default=False)
show_all_experience = ClientStateVar.create("show_all_experience", default=False)
show_all_training = ClientStateVar.create("show_all_training", default=False)
show_all_publications = ClientStateVar.create("show_all_publications", default=False)


def t(es_text: str, en_text: str) -> rx.Var:
    """Return reactive text based on current client-side language selection."""
    return rx.cond(is_spanish.value, es_text, en_text)
