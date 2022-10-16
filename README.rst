======================
 sphinxcontrib-jquery
======================

.. image:: https://img.shields.io/pypi/v/sphinxcontrib-jquery.svg
   :target: https://pypi.org/project/sphinxcontrib-jquery/
   :alt: Package on PyPI

``sphinxcontrib-jquery`` ensures that jQuery is always installed for use in
Sphinx themes or extensions.

To use it, add ``sphinxcontrib.jquery`` as a Sphinx extension:

.. code:: python

   # conf.py

   extensions = [
       "sphinxcontrib.jquery",
   ]
   ...
