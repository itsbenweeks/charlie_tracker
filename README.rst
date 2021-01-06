===============
Charlie Tracker
===============


.. image:: https://img.shields.io/pypi/v/charlie_tracker.svg
        :target: https://pypi.python.org/pypi/charlie_tracker

.. image:: https://img.shields.io/travis/itsbenweeks/charlie_tracker.svg
        :target: https://travis-ci.com/itsbenweeks/charlie_tracker

.. image:: https://readthedocs.org/projects/charlie-tracker/badge/?version=latest
        :target: https://charlie-tracker.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




MBTA Tracker for the command line!


* Free software: MIT license

Installation
------------

With python v3.5+ and pip, run the following in shell:

..code-block:: shell
$ cd directory/of/charlie_tracker/
$ pip3 install .

Alternatively, you can install it from github with `pip install
git+https://github.com/itsbenweeks/charlie_tracker`.


Features/Usage
--------------
.. code-block:: shell
$ charlie_tracker --help
usage: charlie_tracker [-h] {get_routes,get_stops_for_route} ...

Run a charlie_tracker action.

optional arguments:
  -h, --help            show this help message and exit

Actions:
  Valid actions

  {get_routes,get_stops_for_route}
    get_routes          Get routes available to Charlie Tracker
    get_stops_for_route
                        Get stops along a route.


While the use of an API key is optional for the MBTA API, this script will look
for one under the `CT_API_KEY` environment variable and use it in HTTP request
headers.

* TODO
  * Populate the documentation
  * Convert argparse usage to click
  * Write unittests



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
