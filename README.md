Charlie Tracker
===============

MBTA Tracker for the command line.


* Free software: MIT license

Installation
------------

With python v3.5+ and pip, run the following in shell:

```sh
$ cd directory/of/charlie_tracker/
$ pip3 install .
```

Alternatively, you can install it from github with `pip3 install
git+https://github.com/itsbenweeks/charlie_tracker`.


Features/Usage
--------------
```sh
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

While the use of an API key is optional for the MBTA API, this script will look
for one under the `CT_API_KEY` environment variable and use it in HTTP request
headers.

* TODO
  * Populate the documentation
  * Convert argparse usage to click
  * Write unittests



Credits
-------

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template.

Cookiecutter: https://github.com/audreyr/cookiecutter
`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
