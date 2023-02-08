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


Configuration
-------------

.. code:: python

    # Enable Subresource Integrity (SRI) such that
    # <script ... integrity="<hash>"> are included on JS files
    # See more: https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity
    # Default: False

    jquery_sri_enable = True

