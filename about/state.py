import reflex as rx

class State(rx.State):
    """The app state."""
    is_spanish: bool = False  # Default state is English

    def toggle_language(self):
        """Toggle between English and Spanish."""
        self.is_spanish = not self.is_spanish