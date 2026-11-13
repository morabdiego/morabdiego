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
    MUTED = "#4a483f"
    SECONDARY = "#246a4c"
    ACCENT = "#64b692"
    UNEXPECTED = "#8f4040"


class Font(Enum):
    """Editorial pairing: Bitter for headings & display, Montserrat for body, JetBrains Mono for code"""
    HEADING = "'Bitter', Georgia, serif"
    BODY = "'Montserrat', sans-serif"
    MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"


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
    "https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,500..800;1,500..700&family=JetBrains+Mono:wght@500;600&family=Montserrat:ital,wght@0,400..700;1,400..600&display=swap"
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
        "--quote-font-family": Font.HEADING.value,
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
    "::selection": {
        "background": AltColor.ACCENT_SOFT.value,
        "color": AltTextColor.PRIMARY.value,
    },
    "a:focus-visible, button:focus-visible": {
        "outline": f"2px solid {Color.ACCENT.value}",
        "outline_offset": "3px",
    },
    "p, span, a, button, li": {
        "font_family": Font.BODY.value,
    },
    "h1, h2, h3, h4, h5, h6": {
        "font_family": Font.HEADING.value,
    },
}

CARD_STYLE = {
    "background": AltColor.CARD_BG.value,
    "border": f"1px solid {AltColor.BORDER_STRONG.value}",
    "border_radius": "12px",
    "padding": ["1.35rem", "1.65rem", "2rem"],
    "box_shadow": "0 1px 3px rgba(30, 30, 30, 0.04)",
    "transition": "border-color 0.2s ease, transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease",
    "_hover": {
        "transform": "translateY(-2px)",
        "box_shadow": "0 10px 24px -8px rgba(30, 30, 30, 0.08)",
        "border_color": Color.ACCENT.value,
    },
}
