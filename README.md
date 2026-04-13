# Global Hub Dashboard (ALIGN)

This is a Python-based Shiny application for the Global Hub Dashboard. It visualizes innovation pipeline data, readiness assessments, and impact analysis.

## Prerequisites

-   Python 3.11+
-   uv (Python package manager by Astral)

Install uv:

``` bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

## Setup Instructions

1.  Clone the repository

``` bash
git clone <repo-url>
cd <repo-folder>
```

2.  Install dependencies and create environment

``` bash
uv sync
```

This will: - create a virtual environment automatically - install
dependencies from `pyproject.toml` - use `uv.lock` for reproducibility

## Running the Application

``` bash
uv run shiny run app.py
```

The application will start, and you should see a URL (typically
http://127.0.0.1:8000) in the terminal.

## Dependency Management

Add new packages:

``` bash
uv add <package>
```

Update dependencies:

``` bash
uv lock --upgrade
uv sync
```

Pin Python version (optional):

``` bash
uv python pin 3.11
```

## Project Structure

-   `app.py`: Main application entry point (Python Shiny)
-   `modules/`: UI and server modules for dashboard components
-   `utils/`: Helper functions (data loading, theming, UI helpers)
-   `www/`: Static assets and data files
-   `content/`: Quarto documentation content
-   `docs/`: Rendered documentation site (GitHub Pages)
-   `pyproject.toml`: Project dependencies and configuration
-   `uv.lock`: Locked dependency versions for reproducibility

## Notes

-   This project uses `pyproject.toml` + `uv.lock` as the source of
    truth for dependencies.
-   `requirements.txt` is optional and provided only for compatibility.