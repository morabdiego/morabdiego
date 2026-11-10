import os
import reflex as rx

config = rx.Config(
    app_name="about",
    frontend_port=int(os.environ.get("FRONTEND_PORT", 3000)),
    frontend_path=os.environ.get("REFLEX_FRONTEND_PATH", ""),
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="light",
                accent_color="jade",
                radius="large",
            )
        ),
    ],
)
