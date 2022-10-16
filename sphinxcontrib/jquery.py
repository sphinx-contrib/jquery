import sphinx

__version__ = "1.0.0"
version_info = (1, 0, 0)


def setup(app: "sphinx.application.Sphinx"):
    jquery_installed = getattr(app, "_sphinxcontrib_jquery_installed", False)
    if sphinx.version_info[:2] >= (6, 0) and not jquery_installed:
        app.add_js_file(
            "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js",
            priority=100,
        )
        app._sphinxcontrib_jquery_installed = True

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": "1.0.0",
    }
