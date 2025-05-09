import reflex as rx
from enum import Enum

class Color(Enum):
    """Main color scheme - Dark theme (Navbar & Footer)"""
    BACKGROUND = "#1e1e1e"
    PRIMARY = "#f0eedc"
    SECONDARY = "#64b692"
    ACCENT = "#64b692"

class TextColor(Enum):
    """Text colors for dark theme"""
    PRIMARY = "#f0eedc"
    SECONDARY = "#64b692"
    ACCENT = "#64b692"

class AltColor(Enum):
    """Alternative color scheme - Light theme (Content sections)"""
    BACKGROUND = "#f0eedc"
    PRIMARY = "#1e1e1e"
    SECONDARY = "#64b692"
    ACCENT = "#64b692"

class AltTextColor(Enum):
    """Text colors for light theme"""
    PRIMARY = "#1e1e1e"
    SECONDARY = "#64b692"
    ACCENT = "#64b692"
    UNEXPECTED = "#9b4d4d"

class Size(Enum):
    SMALL = "0.7em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    LITTLE_HUGE = "10.4em"
    MID_HUGE = "12em"
    HUGE = "16em"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap"
]
