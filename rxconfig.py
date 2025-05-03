import reflex as rx
import os

config = rx.Config(
    app_name="about",
    show_built_with_reflex=False,
    frontend_port=int(os.environ.get("FRONTEND_PORT", 3000)),
    backend_port=int(os.environ.get("BACKEND_PORT", 8000)),
)