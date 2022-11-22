import json
import requests
from typing import Union


def _get_data_from_api(api_endpoint) -> Union[list, None]:
    api_url = f"https://svc.metrotransit.org{api_endpoint}"
    response = requests.get(url=api_url, timeout=10)
    if response.status_code != 200:
        return None
    return json.loads(response.content)


def get_routes() -> Union[list, None]:
    route_data = _get_data_from_api(
        api_endpoint="/NexTrip/Routes?format=json")

    return route_data


def get_stops_for_route_and_direction(route: str, direction: int) -> Union[list, None]:
    stops_data = _get_data_from_api(
        api_endpoint=f"/NexTrip/Stops/{route}/{direction}?format=json")

    if stops_data is None:
        return None

    return stops_data


def get_next_departure(route: str, direction: int, stop: str) -> Union[dict, None]:
    """Requests the bus stop times for a given route, direction and stop.

    Keyword arguments:

    route       --      the Route value of the bus corresponding
                        to the metrotranist API /NexTrip/Routes endpoint

    direction   --      a Direction integer corresponding to a cardinal
                        direction (1: south, 2: east, 3: west, 4: north)

    stop        --      the Value value of a stop on the given route
                        corresponding to the metrotransit API 
                        /NexTrip/Stops/{Route}/{Direction}

    Data:
    List of objects containing the DepartureTime, Description, Route, RouteDirection etc.
    The list is ordered chronologically by arrival time, soonest first.

    Logic:
    Requests the list of buses given the route, direction and stop from the API

    If the response is :ok, gets the first bus from the list of buses, which is the next arrival.

    Returns:
    -None if the API request returns None or an empty dataset

    -dictionary of the first entry that is returned from the API response.
    """
    departure_data = _get_data_from_api(
        api_endpoint=f"/NexTrip/{route}/{direction}/{stop}?format=json")

    if departure_data is not None and len(departure_data) >= 1:
        next_departure = departure_data[0]
        return next_departure

    return None
