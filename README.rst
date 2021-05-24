=================================
sphinxcontrib-seometatwitter
=================================

Embed `Twitter <https://twitter.com/>`_ comments in Sphinx documents/pages.

Automatically create meta info
Automatically create SEO tags

* Python 2.7, PyPy, 3.7, 3.8, and 3.9 supported on Linux and OS X.
* Python 2.7, 3.7, 3.8, and 3.9 supported on Windows (both 32 and 64 bit versions of Python).

📖 Full documentation: https://coding-to-music.github.io/sphinxcontrib-seometatwitter

.. image:: https://img.shields.io/appveyor/ci/coding-to-music/sphinxcontrib-seometatwitter/master.svg?style=flat-square&label=AppVeyor%20CI
    :target: https://ci.appveyor.com/project/coding-to-music/sphinxcontrib-seometatwitter
    :alt: Build Status Windows

.. image:: https://img.shields.io/travis/coding-to-music/sphinxcontrib-seometatwitter/master.svg?style=flat-square&label=Travis%20CI
    :target: https://travis-ci.org/coding-to-music/sphinxcontrib-seometatwitter
    :alt: Build Status

.. image:: https://img.shields.io/coveralls/coding-to-music/sphinxcontrib-seometatwitter/master.svg?style=flat-square&label=Coveralls
    :target: https://coveralls.io/github/coding-to-music/sphinxcontrib-seometatwitter
    :alt: Coverage Status

.. image:: https://img.shields.io/pypi/v/sphinxcontrib-seometatwitter.svg?style=flat-square&label=Latest
    :target: https://pypi.python.org/pypi/sphinxcontrib-seometatwitter
    :alt: Latest Version

|Build Status| |PyPI version| |Downloads| |License: BSD|



Installing
------------------

Directly install via pip by using::

    pip install sphinx-seometatwitter

Add ``sphinx_seometatwitter`` to the `extensions`_ array in your Sphinx **conf.py**.
For example::

    extensions = ['sphinx_seometatwitter']

.. code:: bash

    pip install sphinxcontrib-seometatwitter

.. changelog-section-start

Changelog
------------------

This project adheres to `Semantic Versioning <http://semver.org/>`_.

0.6.0 - 2021-05-23
------------------

* Initial release.

.. changelog-section-end

See Who Is Using It
-------------------

You can use `GitHub search`_ or `libraries.io`_ to see who is using
**sphinx-sitemap**.

Contributing
------------------

Pull Requests welcome! See `CONTRIBUTING`_ for instructions on how best to
contribute.

Maintaining PyPI Version
------------------------

These are the steps, to be run by the maintainer, for making a new Python
package release.

#. Rev versions in **sphinx_seometatwitter/version.py** and **setup.py**.
#. Update **CHANGELOG.md**
#. Create a tag and push to GitHub::

       git tag -a vX.Y.Z -m "Release vX.Y.Z"
       git push --tags origin master

#. Create latest distribution locally::

       python setup.py sdist

#. Upload to the test pypi.org repository::

       twine upload --repository-url https://test.pypi.org/legacy/ dist/*

#. Upload to the production pypi.org repository::

       twine upload dist/*


License
-------

**sphinx-seometatwitter** is made available under a **BSD license**; see `LICENSE`_ for
details.

Originally based on the sphinx_twitter generator in the `sphinx_twitter`_ project. 

.. _CONTRIBUTING: CONTRIBUTING.md
.. _sphinx_twitter: https://pypi.org/project/sphinxcontrib.twitter/
.. _extensions: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
.. _GitHub search: https://github.com/search?utf8=%E2%9C%93&q=sphinx-seometatwitter+extension%3Atxt&type=
.. _gitpython: https://gitpython.readthedocs.io/en/stable/
.. _html_extra_path: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path
.. _language: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
.. _libraries.io: https://libraries.io/pypi/sphinx-seometatwitter
.. _LICENSE: LICENSE
.. _Sphinx: http://sphinx-doc.org/
.. _time format: https://docs.python.org/2/library/time.html#time.strftime

.. |Build Status| image:: https://travis-ci.org/jdillard/sphinx-seometatwitter.svg?branch=master
   :target: https://travis-ci.org/jdillard/sphinx-seometatwitter
.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-seometatwitter.svg
   :target: https://pypi.python.org/pypi/sphinx-seometatwitter
.. |Downloads| image:: https://pepy.tech/badge/sphinx-seometatwitter/week
    :target: https://pepy.tech/project/sphinx-seometatwitter
.. |License: BSD| image:: https://img.shields.io/badge/License-BSD-blue.svg
   :target: https://github.com/jdillard/sphinx-seometatwitter/blob/master/LICENSE

       