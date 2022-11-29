import json
import requests

API = "https://svc.metrotransit.org/nextripv2"

def _get_data_from_api(api_endpoint):
    api_url = f"{API}{api_endpoint}"
    try:
        response = requests.get(url=api_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise requests.exceptions.HTTPError(err) from err
    
    except requests.exceptions.ConnectionError as err:
        raise requests.exceptions.ConnectionError(err) from err

    try: 
        data = json.loads(response.content)
    except ValueError as err:
        raise ValueError(err) from err
    
    return data


def get_routes() -> list:
    route_data = _get_data_from_api(
        api_endpoint="/routes")
    return route_data


def get_directions_for_route(route_id) -> list:
    direction_data = _get_data_from_api(api_endpoint=f"/directions/{route_id}")
    return direction_data


def get_stops_for_route_and_direction(route_id: str, direction_id: int) -> list:
    stops_data = _get_data_from_api(
        api_endpoint=f"/stops/{route_id}/{direction_id}")
    return stops_data


def get_departures(route_id: str, direction_id: int, place_code: str) -> list:
    """Requests the bus stop times for a given route, direction and stop.

    Keyword arguments:

    route_id       --   the route value of the bus corresponding
                        to the metrotranist API /nextripv2/routes endpoint

    direction_id   --   a direction integer corresponding to a valid cardinal
                        direction the route travels (north and south or east and west)

    place_code     --   the place_code value of a stop on the given route
                        corresponding to the metrotransit API 
                        /nextripv2/stops/{route_id}/{direction_id}

    Data:

    Dictionary of objects containing the stops, alerts and departures for the 
    given route_id, direction_id and place_code.
    The list of departures is ordered chronologically by arrival time, soonest first.

    Logic:

    Requests the list of buses given the route_id, direction_id and place_code from the API

    If the response is :ok, gets the list of departures.

    Returns:

    -   List of departures that are returned from the API response.
    
    -   Empty List if API response has no "departures" key.
    """

    departures = _get_data_from_api(
        api_endpoint=f"/{route_id}/{direction_id}/{place_code}")
    return departures.get("departures", [])
