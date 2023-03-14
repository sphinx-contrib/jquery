Release 4.1 (14/03/2023)
==========================

* Include ``tests/``, ``AUTHORS``, ``CHANGES.rst``, and ``LICENCE`` in the
  source distribution ('sdist') file. No changes to functionality.

Release 4.0 (14/03/2023)
==========================

* Enforcing `subresource integrity`_ (SRI) checks breaks loading rendered
  documentation from local filesystem (``file:///`` URIs).
  SRI checks may now be configured by the boolean configuration option
  ``jquery_use_sri``, which defaults to ``False``.
  See `sphinx_rtd_theme#1420`_ for further details.

.. _sphinx_rtd_theme#1420: https://github.com/readthedocs/sphinx_rtd_theme/issues/1420

Release 3.0.0 (03/11/2022)
==========================

* Vendor jQuery within the extension and copy the files to the documentation's
  ``_static`` directory.
* Include the ``_sphinx_javascript_frameworks_compat.js`` compatibility file
  from Sphinx 5.
* Include `subresource integrity`_ checksums in generated ``<script/>`` tags.

.. _subresource integrity: https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity

Release 2.0.0 (18/10/2022)
==========================

* Declare support for Python 2.7, 3.5, and 3.6.
* Add testing.

Release 1.0.0 (17/10/2022)
==========================

* Initial release of ``sphinxcontrib-jquery``.
