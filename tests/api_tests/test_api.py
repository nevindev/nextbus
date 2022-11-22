from api import api

VALID_API_ENDPOINT = "/NexTrip/Routes?format=json"
INVALID_API_ENDPOINT = "/this/does/not/exist"

VALID_ROUTE = "901"
VALID_STOP = "TF2"
VALID_DIRECTION = 1

INVALID_ROUTE = "FakeRoute"
INVALID_STOP = "FAKE"
INVALID_DIRECTION = 5


def test_get_data_from_api_with_valid_endpoint_returns_object():
    data = api._get_data_from_api(api_endpoint=VALID_API_ENDPOINT)
    assert isinstance(data, list) is True


def test_get_data_from_api_with_invalid_endpoint_returns_none():
    data = api._get_data_from_api(api_endpoint=INVALID_API_ENDPOINT)
    assert data is None


def test_get_stops_for_route_and_direction_with_valid_input_returns_list():
    stops = api.get_stops_for_route_and_direction(route=VALID_ROUTE, direction=VALID_DIRECTION)
    assert isinstance(stops, list)


def  test_get_stops_for_route_and_direction_with_invalid_inputs_returns_none():
    invalid_route = api.get_stops_for_route_and_direction(route=INVALID_ROUTE, direction=VALID_DIRECTION)
    assert invalid_route is None

    invalid_direction = api.get_stops_for_route_and_direction(route=VALID_ROUTE, direction=INVALID_DIRECTION)
    assert invalid_direction is None

    invalid = api.get_stops_for_route_and_direction(route=INVALID_ROUTE, direction=INVALID_DIRECTION)
    assert invalid is None


def test_get_next_departure_with_valid_input_returns_dict():
    departure = api.get_next_departure(route=VALID_ROUTE, direction=VALID_DIRECTION, stop=VALID_STOP)
    assert isinstance(departure, dict)


def test_get_next_departure_with_invalid_inputs_returns_none():
    invalid_route_departure = api.get_next_departure(route=INVALID_ROUTE, direction=VALID_DIRECTION, stop=VALID_STOP)
    assert invalid_route_departure is None

    invalid_stop_departure = api.get_next_departure(route=VALID_ROUTE, direction=VALID_DIRECTION, stop=INVALID_STOP)
    assert invalid_stop_departure is None

    invalid_direction_departure = api.get_next_departure(route=VALID_ROUTE, direction=INVALID_DIRECTION, stop=VALID_STOP)
    assert invalid_direction_departure is None

    invalid_departure = invalid_stop_departure = api.get_next_departure(route=INVALID_ROUTE, direction=INVALID_DIRECTION, stop=INVALID_STOP)
    assert invalid_departure is None