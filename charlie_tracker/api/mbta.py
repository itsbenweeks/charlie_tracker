"""MBTA module."""
import requests

class MBTAException(Exception):
    """Base exception class others inherit"""
    pass

class MBTABadRequest(MBTAException):
    """400 Status code was thrown"""
    pass

class MBTAForbidden(MBTAException):
    """403 Status code was thrown"""
    pass

class MBTATooManyRequests(MBTAException):
    """429 Satus code was thrown"""
    pass

class MBTAWrongRouteId(MBTAException):
    """The route id passed doesn't exist"""
    pass

class MBTAUnknownError(MBTAException):
    """Unexpected status code exception"""
    pass

class MBTAEmptyResult(MBTAException):
    """Response unexpectedly had an empty result"""
    pass

class MBTA(object):
    """
    API Class for handling calls to MBTA.org
    """

    def __init__(self, api_key: str = None) -> None:
        """Initialize a requests sesssion for use with this class by specifying
        the base API endpoint and key.

        Args:
            api_key (str): MBTA API key
        """

        self.api_url = 'https://api-v3.mbta.com'
        self.session = requests.Session()
        if api_key:
            self.session.headers = {
                'x-api-key': api_key,
                'User-Agent': 'Charlie Tracker',
            }
        self.session.params = {'page[limit]': 50}

    def _get_all(self, url: str, params: dict = None) -> list:
        """Return all results from URL given (i.e. page through them)

        Args:
            url(str): Full MBTA URL with results.
        Raises:
            requests.exceptions.RequestException
            MBTABadRequest
            MBTAForbidden
            MBTATooManyRequests
            MBTAUnknownError
        Returns:
            list: List of items returned.
        """
        results = None
        response = self.session.get(url, params = params)
        if response.status_code == 200:
            results = response.json()['data']
            response_json = response.json()
            while (
                'links' in response_json and
                response_json['links'].get('next', False) and
                response.status_code == 200
            ):
                response = self.session.get(
                    response_json['links']['next'],
                    params = params
                )
                response_json = response.json()
                results += response_json['data']
        else:
            exceptions_map = {
                400: MBTABadRequest,
                403: MBTAForbidden,
                423: MBTATooManyRequests,
            }
            if response.status_code not in exceptions_map.keys():
                raise MBTAUnknownError(response.text)
            raise exceptions_map[response.status_code](response.text)
        if len(results) == 0:
            raise MBTAEmptyResult("Request had an unexpected empty result.")
        return results

    def get_routes(self) -> list:
        """Return a list of routes objects

        Raises:
            requests.exceptions.RequestException
            MBTABadRequest
            MBTAForbidden
            MBTATooManyRequests
            MBTAUnknownError

        Returns:
            list: `data` list from routes dictionary
                  (https://api-v3.mbta.com/docs/swagger/index.html#/Route/ApiWeb_RouteController_index)
        """
        routes_url = f'{self.api_url}/routes'
        return self._get_all(routes_url)

    def get_stops_for_route(self, route_id: str) -> list:
        """Return a list of stops.

        Raises:
            requests.exceptions.RequestException
            MBTABadRequest
            MBTAForbidden
            MBTATooManyRequests
            MBTAUnknownError

        Returns:
            list: A list of stops from the `data` object of the endpoint's
            response.
        """
        params = {'filter[route]': route_id}
        stops_url = f'{self.api_url}/stops'
        return self._get_all(stops_url, params)
