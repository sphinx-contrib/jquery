from pathlib import Path

import pytest
import sphinx
from sphinx.testing.path import path
from sphinx.testing.util import SphinxTestApp


def run_blank_app(srcdir, **kwargs):
    Path(srcdir, "conf.py").write_text("", encoding="ascii")
    Path(srcdir, "index.rst").write_text("", encoding="ascii")
    app = SphinxTestApp(**kwargs, srcdir=srcdir)
    app.builder.build_all()
    app.cleanup()
    return Path(srcdir, "_build", "html")


@pytest.fixture(scope="function")
def blank_app(tmpdir, monkeypatch):
    def inner(**kwargs):
        return run_blank_app(path(tmpdir), **kwargs)

    monkeypatch.setattr("sphinx.application.abspath", lambda x: x)
    yield inner


@pytest.mark.skipif(sphinx.version_info[:2] < (6, 0),
                    reason="Requires Sphinx 6.0 or greater")
def test_jquery_installed_sphinx_ge_60(blank_app):
    out_dir = blank_app(confoverrides={"extensions": ["sphinxcontrib.jquery"]})

    text = out_dir.joinpath("index.html").read_text(encoding="utf-8")
    assert '<script src="_static/jquery.js"></script>' in text
    assert '<script src="_static/_sphinx_javascript_frameworks_compat.js"></script>' in text

    static_dir = out_dir / '_static'
    assert static_dir.joinpath('jquery.js').is_file()
    assert static_dir.joinpath('_sphinx_javascript_frameworks_compat.js').is_file()


@pytest.mark.skipif(sphinx.version_info[:2] >= (6, 0),
                    reason="Requires Sphinx older than 6.0")
def test_jquery_installed_sphinx_lt_60(blank_app):
    out_dir = blank_app(confoverrides={"extensions": ["sphinxcontrib.jquery"]})

    text = out_dir.joinpath("index.html").read_text(encoding="utf-8")
    assert '<script src="_static/jquery.js"></script>' in text
    if sphinx.version_info[:1] == (5,):
        assert '<script src="_static/_sphinx_javascript_frameworks_compat.js"></script>' in text

    static_dir = out_dir / '_static'
    assert static_dir.joinpath('jquery.js').is_file()
    if sphinx.version_info[:1] == (5,):
        assert static_dir.joinpath('_sphinx_javascript_frameworks_compat.js').is_file()
