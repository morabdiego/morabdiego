from enum import Enum


class Color(Enum):
    """Main color scheme - Dark theme (Navbar, Footer, & Dark surfaces)"""
    BACKGROUND = "#1e1e1e"
    BACKGROUND_DEEP = "#141414"
    SURFACE = "#282828"
    PRIMARY = "#f0eedc"
    SECONDARY = "#64b692"
    ACCENT = "#64b692"
    BORDER = "rgba(240, 238, 220, 0.14)"


class TextColor(Enum):
    """Text colors for dark theme"""
    PRIMARY = "#f0eedc"
    MUTED = "#b5b2a0"
    SECONDARY = "#64b692"
    ACCENT = "#64b692"


class AltColor(Enum):
    """Alternative color scheme - Warm light theme (Content sections)"""
    BACKGROUND = "#f0eedc"
    BACKGROUND_ALT = "#e6e3cd"
    CARD_BG = "#fbfaf3"
    PRIMARY = "#1e1e1e"
    SECONDARY = "#64b692"
    ACCENT = "#64b692"
    ACCENT_DARK = "#2b7a58"
    ACCENT_SOFT = "rgba(100, 182, 146, 0.18)"
    HIGHLIGHT_SOFT = "rgba(155, 77, 77, 0.12)"
    BORDER = "rgba(30, 30, 30, 0.09)"
    BORDER_STRONG = "rgba(30, 30, 30, 0.16)"


class AltTextColor(Enum):
    """Text colors for light theme"""
    PRIMARY = "#1e1e1e"
    MUTED = "#545249"
    SECONDARY = "#2b7a58"
    ACCENT = "#64b692"
    UNEXPECTED = "#9b4d4d"


class Font(Enum):
    """Unified Montserrat typography across the entire site"""
    HEADING = "'Montserrat', sans-serif"
    BODY = "'Montserrat', sans-serif"
    MONO = "'Montserrat', sans-serif"


class Size(Enum):
    SMALL = "0.75em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    VERY_BIG = "3.5em"
    LITTLE_HUGE = "10.4em"
    MID_HUGE = "12em"
    HUGE = "16em"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300..900;1,300..700&display=swap"
]

GLOBAL_STYLE = {
    "html": {
        "scroll_behavior": "smooth",
        "font_family": Font.BODY.value,
    },
    ":root, .radix-themes": {
        "--default-font-family": Font.BODY.value,
        "--heading-font-family": Font.HEADING.value,
        "--code-font-family": Font.MONO.value,
        "--strong-font-family": Font.BODY.value,
        "--em-font-family": Font.BODY.value,
        "--quote-font-family": Font.BODY.value,
        "font_family": Font.BODY.value,
    },
    "body": {
        "font_family": Font.BODY.value,
        "background_color": AltColor.BACKGROUND.value,
        "color": AltTextColor.PRIMARY.value,
        "margin": "0",
        "padding": "0",
        "overflow_x": "hidden",
        "-webkit-font-smoothing": "antialiased",
    },
    "h1, h2, h3, h4, h5, h6, p, span, a, button, li": {
        "font_family": Font.BODY.value,
    },
}

CARD_STYLE = {
    "background": AltColor.CARD_BG.value,
    "border": f"1px solid {AltColor.BORDER.value}",
    "border_radius": "18px",
    "padding": ["1.5rem", "1.75rem", "2.25rem"],
    "box_shadow": "0 8px 24px -4px rgba(30, 30, 30, 0.05), 0 2px 6px -1px rgba(30, 30, 30, 0.03)",
    "transition": "all 0.25s cubic-bezier(0.16, 1, 0.3, 1)",
    "_hover": {
        "transform": "translateY(-3px)",
        "box_shadow": "0 16px 32px -6px rgba(30, 30, 30, 0.09), 0 4px 10px -2px rgba(30, 30, 30, 0.04)",
        "border_color": Color.ACCENT.value,
    },
}
