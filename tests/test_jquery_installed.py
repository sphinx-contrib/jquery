import os.path

import pytest
import sphinx
from sphinx.testing.path import path
from sphinx.testing.util import SphinxTestApp


def run_blank_app(srcdir, **kwargs):
    with open(os.path.join(srcdir, "conf.py"), "w", encoding="ascii") as f:
        f.write("")
    with open(os.path.join(srcdir, "index.rst"), "w", encoding="ascii") as f:
        f.write("")
    app = SphinxTestApp(
        **kwargs,
        srcdir=srcdir
    )
    app.builder.build_all()
    app.cleanup()
    with open(os.path.join(srcdir, "_build", "html", "index.html"), "r", encoding="utf-8") as f:
        text = f.read()
    return text


@pytest.fixture(scope="function")
def blank_app(tmpdir, monkeypatch):
    def inner(**kwargs):
        return run_blank_app(path(tmpdir), **kwargs)

    monkeypatch.setattr("sphinx.application.abspath", lambda x: x)
    yield inner


@pytest.mark.skipif(sphinx.version_info[:2] < (6, 0),
                    reason="Requires Sphinx 6.0 or greater")
def test_jquery_installed_sphinx_ge_60(blank_app):
    text = blank_app(confoverrides={"extensions": ["sphinxcontrib.jquery"]})
    assert "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js" in text


@pytest.mark.skipif(sphinx.version_info[:2] >= (6, 0),
                    reason="Requires Sphinx older than 6.0")
def test_jquery_installed_sphinx_lt_60(blank_app):
    text = blank_app(confoverrides={"extensions": ["sphinxcontrib.jquery"]})
    assert "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js" not in text
