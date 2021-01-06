"""Main module."""
from charlie_tracker import config
from charlie_tracker.lib import MBTA, MBTAEmptyResult

def print_routes() -> None:
    """Calls the `/routes` endpoint and prints the `id` and `long_name` of
    each idividual route:

    Raises:
        requests.RequestException
        charlie_tracker.lib.MBTAUnknownError
        charlie_tracker.lib.MBTAInvalidRouteID
    """
    mbta = MBTA(config.CT_MBTA_API_KEY)
    routes = mbta.get_routes()
    title_text = f"List of Routes on MBTA"
    print(f"{title_text:=^80}")
    for route in routes:
        print(
            f"ID: {route['id']}, NAME: {route['attributes']['long_name']}"
        )
    return

def print_stops_for_route(route_id: str) -> None:
    """Calls the `/stops` endpoint with a filter parameter for a given stop
    """
    mbta = MBTA(config.CT_MBTA_API_KEY)
    try:
        stops = mbta.get_stops_for_route(route_id)
    except MBTAEmptyResult:
        print(f"Route '{route_id}' returned no results")
        return
    title_text = f"Stops for '{route_id}'"
    print(f"{title_text:=^80}")
    for stop in stops:
        print(f"ID: {stop['id']}, NAME: {stop['attributes']['name']}")
    return
