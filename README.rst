wkhtmltopdf-pack
================

This package installs a `wkhtmltopdf` binary in a Heroku or cloudControl deployment. Versioning on this package mimics
the version number of the included `wkhtmltopdf` binary.

wkhtmltopdf_ is an open source (LGPLv3) command line tool to render HTML into PDF using the
Qt WebKit rendering engine.

Installation
------------

Install it in the usual way:

    pip install wkhtmltopdf-pack

Usage
-----

There are multiple Python wrappers for wkhtmltopdf you can use. If you are using Django in your project, you can use
the django-wkhtmltopdf_ wrapper.

The binary you want to use is named `wkhtmltopdf-pack`.

Acknowledgements
----------------

Binaries are originally generated for the `wkhtmltopdf-heroku` Ruby Gem. A big thank you to the wkhtmltopdf-heroku_
contributors!


.. _wkhtmltopdf: http://wkhtmltopdf.org/
.. _django-wkhtmltopdf: https://pypi.python.org/pypi/django-wkhtmltopdf
.. _wkhtmltopdf-heroku: https://github.com/bradphelan/wkhtmltopdf-heroku
