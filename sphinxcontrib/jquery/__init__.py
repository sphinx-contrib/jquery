from os import makedirs, path
import shutil

import sphinx

__version__ = "3.0.0"
version_info = (3, 0, 0)

_ROOT_DIR = path.abspath(path.dirname(__file__))
_FILES = (
    (
        'jquery.js',
        'sha384-vtXRMe3mGCbOeY7l30aIg8H9p3GdeSe4IFlP6G8JMa7o7lXvnz3GFKzPxzJdPfGK',
    ),
    (
        '_sphinx_javascript_frameworks_compat.js',
        'sha384-lSZeSIVKp9myfKbDQ3GkN/KHjUc+mzg17VKDN4Y2kUeBSJioB9QSM639vM9fuY//',
    ),
)


def setup(app):
    jquery_installed = getattr(app, "_sphinxcontrib_jquery_installed", False)
    if sphinx.version_info[:2] >= (6, 0) and not jquery_installed:
        makedirs(path.join(app.outdir, '_static'), exist_ok=True)
        for (filename, integrity) in _FILES:
            app.add_js_file(filename, integrity=integrity, priority=100)
            shutil.copyfile(
                path.join(_ROOT_DIR, filename),
                path.join(app.outdir, '_static', filename)
            )
        app._sphinxcontrib_jquery_installed = True

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
