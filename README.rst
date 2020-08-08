bitranox_coloredlogs
====================


Version v14.0.8 as of 2020-08-08 see `Changelog`_

|travis_build| |license| |jupyter| |pypi|

|codecov| |better_code| |cc_maintain| |cc_issues| |cc_coverage| |snyk|


.. |travis_build| image:: https://img.shields.io/travis/bitranox/bitranox_coloredlogs/master.svg
   :target: https://travis-ci.org/bitranox/bitranox_coloredlogs

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/bitranox/bitranox_coloredlogs/master?filepath=bitranox_coloredlogs.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/bitranox-coloredlogs?label=PyPI%20Package
   :target: https://badge.fury.io/py/bitranox_coloredlogs

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/bitranox_coloredlogs
   :target: https://codecov.io/gh/bitranox/bitranox_coloredlogs

.. |better_code| image:: https://bettercodehub.com/edge/badge/bitranox/bitranox_coloredlogs?branch=master
   :target: https://bettercodehub.com/results/bitranox/bitranox_coloredlogs

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/bitranox_coloredlogs?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/bitranox_coloredlogs/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/bitranox_coloredlogs?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/bitranox_coloredlogs/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/bitranox_coloredlogs?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/bitranox_coloredlogs/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://img.shields.io/snyk/vulnerabilities/github/bitranox/bitranox_coloredlogs
   :target: https://snyk.io/test/github/bitranox/bitranox_coloredlogs

fork of xolox coloredlogs with possibility to log to travis and jupyter

since the parameter *isatty* is not behaving like expected (should FORCE) color, the original version does
not show colors on travis and jupyter(stdout).

with that version You can have colored logs on jupyter and travis.

I hope Peter accepts my PullRequest, then I can delete this stripped (no tests) Version ...


find the original here :   https://coloredlogs.readthedocs.io/en/latest/

----

automated tests, Travis Matrix, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.6.0 or newer

tested on linux "bionic" with python 3.6, 3.7, 3.8, 3.8-dev, pypy3 - architectures: amd64, ppc64le, s390x, arm64

tested under `Linux, macOS, Windows <https://travis-ci.org/bitranox/bitranox_coloredlogs>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/bitranox_coloredlogs/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/bitranox_coloredlogs/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/bitranox_coloredlogs/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/{{rst_include.
repository_slug}}/master?filepath=bitranox_coloredlogs.ipynb>`_

Usage
-----------

.. code-block::

    import the module and check the code - its easy and documented there, including doctest examples.
    in case of any questions the usage section might be expanded at a later time

Usage from Commandline
------------------------

.. code-block:: bash

   can not get help - probably not a proper click application

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools

- to install the latest release from PyPi via pip (recommended):

.. code-block:: bash

    python -m pip install --upgrade bitranox_coloredlogs

- to install the latest version from github via pip:


.. code-block:: bash

    python -m pip install --upgrade git+https://github.com/bitranox/bitranox_coloredlogs.git


- include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    bitranox_coloredlogs

    # for the latest development version :
    bitranox_coloredlogs @ git+https://github.com/bitranox/bitranox_coloredlogs.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/bitranox_coloredlogs.git
    $ cd bitranox_coloredlogs
    python setup.py install

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/bitranox_coloredlogs.git
    $ cd bitranox_coloredlogs

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## project requirements
    click
    humanfriendly >= 7.1

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/bitranox_coloredlogs/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

v14.0.8
--------
2020-08-08: service release
    - fix documentation
    - fix travis
    - deprecate pycodestyle
    - implement flake8

v14.0.7
---------
2020-08-01: fix pypi deploy

v14.0.6
---------
2020-07-31: fix travis build

v14.0.5
---------
2020-07-29: feature release
    - use new pizzacutter template

v14.0.4
---------
2020-07-17: patch release
    - added __init__.pyi file to make minimal type annotations
    - make it a PEP561 package

v14.0.2
---------
2020-07-17: pulling in @EpicWink default stream for TTY-check is stderr

v14.0.1
---------
2020-07-17: patch release
    - make parameter install(isatty=True) forcing ColorFormatter

