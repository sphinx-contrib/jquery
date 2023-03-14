import base64
import hashlib
from pathlib import Path

import pytest
import sphinx
from sphinx.testing.path import path
from sphinx.testing.util import SphinxTestApp

from sphinxcontrib.jquery import _FILES, _ROOT_DIR  # NoQA


def run_blank_app(srcdir, **kwargs):
    Path(srcdir, "conf.py").write_text("", encoding="ascii")
    if sphinx.version_info[:2] >= (2, 0):
        Path(srcdir, "index.rst").touch()
    else:
        Path(srcdir, "contents.rst").touch()
    for _ in range(2):  # build twice to test re-builds
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
def test_jquery_installed_sphinx_ge_60_use_sri(blank_app):
    out_dir = blank_app(confoverrides={"extensions": ["sphinxcontrib.jquery"], "jquery_use_sri": True})

    text = out_dir.joinpath("index.html").read_text(encoding="utf-8")
    assert ('<script '
            'integrity="sha384-vtXRMe3mGCbOeY7l30aIg8H9p3GdeSe4IFlP6G8JMa7o7lXvnz3GFKzPxzJdPfGK" '
            'src="_static/jquery.js"></script>') in text
    assert ('<script '
            'integrity="sha384-lSZeSIVKp9myfKbDQ3GkN/KHjUc+mzg17VKDN4Y2kUeBSJioB9QSM639vM9fuY//" '
            'src="_static/_sphinx_javascript_frameworks_compat.js"></script>') in text

    static_dir = out_dir / '_static'
    assert static_dir.joinpath('jquery.js').is_file()
    assert static_dir.joinpath('_sphinx_javascript_frameworks_compat.js').is_file()


@pytest.mark.skipif(sphinx.version_info[:2] < (6, 0),
                    reason="Requires Sphinx 6.0 or greater")
def test_jquery_installed_sphinx_ge_60(blank_app):
    out_dir = blank_app(confoverrides={"extensions": ["sphinxcontrib.jquery"]})

    text = out_dir.joinpath("index.html").read_text(encoding="utf-8")
    assert ('<script '
            'src="_static/jquery.js"></script>') in text
    assert ('<script '
            'src="_static/_sphinx_javascript_frameworks_compat.js"></script>') in text

    static_dir = out_dir / '_static'
    assert static_dir.joinpath('jquery.js').is_file()
    assert static_dir.joinpath('_sphinx_javascript_frameworks_compat.js').is_file()


@pytest.mark.skipif(sphinx.version_info[:2] >= (6, 0),
                    reason="Requires Sphinx older than 6.0")
def test_jquery_installed_sphinx_lt_60(blank_app):
    out_dir = blank_app(confoverrides={"extensions": ["sphinxcontrib.jquery"]})

    if sphinx.version_info[:2] >= (2, 0):
        text = out_dir.joinpath("index.html").read_text(encoding="utf-8")
        assert '<script src="_static/jquery.js"></script>' in text
    else:
        text = out_dir.joinpath("contents.html").read_text(encoding="utf-8")
        assert '<script type="text/javascript" src="_static/jquery.js"></script>' in text
    if sphinx.version_info[:1] == (5,):
        assert '<script src="_static/_sphinx_javascript_frameworks_compat.js"></script>' in text

    static_dir = out_dir / '_static'
    assert static_dir.joinpath('jquery.js').is_file()
    if sphinx.version_info[:1] == (5,):
        assert static_dir.joinpath('_sphinx_javascript_frameworks_compat.js').is_file()


@pytest.mark.parametrize(('filename', 'integrity'), _FILES, ids=[*dict(_FILES)])
def test_integrity(filename, integrity):
    checksum = hashlib.sha384(Path(_ROOT_DIR, filename).read_bytes())
    encoded = base64.b64encode(checksum.digest()).decode(encoding='ascii')
    assert f"sha384-{encoded}" == integrity
