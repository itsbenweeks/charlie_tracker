"""Console script for charlie_tracker."""
import argparse

from charlie_tracker import actions

def run_get_routes(args):
    """Run the print routes actions using args"""
    routes = actions.print_routes()

def run_get_stops_for_route(args):
    """Run the print stops action using args"""
    routes = actions.print_stops_for_route(args.route_id)

def execute():
    """Execute command line charlie_tracker actions."""
    parser = argparse.ArgumentParser(
        prog='charlie_tracker',
        description = 'Run a charlie_tracker action.\n',
    )
    subparsers = parser.add_subparsers(
        title = "Actions",
        description = "Valid actions",
    )

    # Get routes subparser
    get_routes = subparsers.add_parser(
        'get_routes',
        help='Get routes available to Charlie Tracker'
    )
    get_routes.set_defaults(func=run_get_routes)

    # Get stops for routes subparser
    get_stops_for_route = subparsers.add_parser(
        'get_stops_for_route',
        help='Get stops along a route.'
    )
    get_stops_for_route.add_argument(
        '-r', '--route_id', type=str, required=True,
        help='Route ID to get stops for (i.e. Red)'
    )
    get_stops_for_route.set_defaults(func=run_get_stops_for_route)

    # Run an action
    args = parser.parse_args()
    args.func(args)
