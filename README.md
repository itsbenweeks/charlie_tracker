Charlie Tracker
===============

MBTA Tracker for the command line.


* Free software: MIT license

Installation
------------

With git, python v3.5+, and pip, run the following in shell:

```
$ git clone git@github.com:itsbenweeks/charlie_tracker.git
$ cd charlie_tracker/
$ pip3 install .
$ charlie_tracker -h
```

Alternatively, you can install it from github with `pip3 install
git+https://github.com/itsbenweeks/charlie_tracker`.


Features/Usage
--------------
```
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
```

```
$ charlie_tracker get_routes -h
usage: charlie_tracker get_routes [-h]

optional arguments:
  -h, --help  show this help message and exit
```

```
$ charlie_tracker get_stops_for_route -h
usage: charlie_tracker get_stops_for_route [-h] -r ROUTE_ID

optional arguments:
  -h, --help            show this help message and exit
  -r ROUTE_ID, --route_id ROUTE_ID
                        Route ID to get stops for (i.e. Red)
```

While the use of an API key is optional for the MBTA API, this program will give
users the option to store one under the `CT_MBTA_API_KEY` environment variable
and use it in HTTP request headers. e.g:

```
$ export CT_MBTA_API_KEY=1234567890abcdef
```

* TODO
  * Populate the documentation
  * Convert argparse usage to click
  * Write unittests



Credits
-------

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template.

Cookiecutter: https://github.com/audreyr/cookiecutter
`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
