################
buildbot-badges
################

.. start short_desc

**Fork of buildbot-badges with support for specifying builders by name.**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/domdfcoding/buildbot-badges/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/buildbot-badges/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/buildbot-badges/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/buildbot-badges/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/buildbot-badges/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/buildbot-badges/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/buildbot-badges/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/buildbot-badges/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/buildbot-badges/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/buildbot-badges/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.herokuapp.com/github/domdfcoding/buildbot-badges/badge.svg
	:target: https://dependency-dash.herokuapp.com/github/domdfcoding/buildbot-badges/
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/buildbot-badges?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/buildbot-badges
	:alt: CodeFactor Grade

.. |license| image:: https://img.shields.io/github/license/domdfcoding/buildbot-badges
	:target: https://github.com/domdfcoding/buildbot-badges/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/buildbot-badges
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/buildbot-badges/v2.9.4
	:target: https://github.com/domdfcoding/buildbot-badges/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/buildbot-badges
	:target: https://github.com/domdfcoding/buildbot-badges/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2022
	:alt: Maintenance

.. end shields

Installation
--------------

.. start installation

``buildbot-badges`` can be installed from GitHub.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install git+https://github.com/domdfcoding/buildbot-badges

.. end installation
