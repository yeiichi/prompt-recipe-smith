"""Sphinx configuration for prompt-recipe-smith documentation."""

from __future__ import annotations

project = "prompt-recipe-smith"
author = "Eiichi YAMAMOTO"
release = "0.0.0"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
]

html_theme = "furo"
html_title = "prompt-recipe-smith"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
