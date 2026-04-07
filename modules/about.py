import os
from shiny import ui


# =========================================================
# UTIL
# =========================================================
def load_html(path):
    with open(path, "r") as f:
        html = f.read()

    # Extract only the content within the main tag to avoid including
    # full <html>, <head>, and <body> tags which break host page styling.
    start_tag = '<main class="content" id="quarto-document-content">'
    end_tag = "</main>"

    start_idx = html.find(start_tag)
    end_idx = html.find(end_tag)

    if start_idx != -1 and end_idx != -1:
        content = html[start_idx : end_idx + len(end_tag)]

        # Clean up unrendered Quarto/R artifacts if they exist
        content = content.replace("<code>r params$last_updated</code>", "2026-03-27")
        content = content.replace("`r params$last_updated`", "2026-03-27")

        return content

    return html


# =========================================================
# LOAD CONTENT (CACHE AT IMPORT)
# =========================================================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ABOUT_PATH = os.path.join(BASE_DIR, "docs", "content", "about.html")

ABOUT_HTML = load_html(ABOUT_PATH)


# =========================================================
# UI
# =========================================================

def about_ui(id):

    return ui.div(
        ui.div(
            ui.HTML(ABOUT_HTML),
            class_="about-body",
            style="""
                width: 100%;
            """,
        ),
        class_="container-fluid px-4 py-4",
    )