# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "淡々と"
copyright = "2024, Tanimoto Masashi"
author = "Tanimoto Masashi"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.mermaid",
    "sphinxemoji.sphinxemoji",
    "sphinx_copybutton",
    "sphinx_sitemap",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = "https://tnmt-1.github.io/memo/"
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = [
    "stylesheets/custom.css",
]
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"
html_show_sourcelink = False

html_theme_options = {
    "logo": {
        "image_light": "_static/logo.png",
        "image_dark": "_static/logo.png",
        "text": "淡々と",
    }
}
