import pytest

from api import api

# VALID_API_ENDPOINT_V1 = "/NexTrip/Routes?format=json"
VALID_API_ENDPOINT_V2 = "/routes"
INVALID_API_ENDPOINT = "/this/does/not/exist"

VALID_ROUTE_ID = "901"
VALID_PLACE_CODE = "TF2"
VALID_DIRECTION_ID = 1

INVALID_ROUTE_ID = "FakeRoute"
INVALID_PLACE_CODE = "FAKE"
INVALID_DIRECTION_ID = 5


def test_get_data_from_api_with_valid_endpoint_returns_object():
    data = api._get_data_from_api(api_endpoint=VALID_API_ENDPOINT_V2)
    assert isinstance(data, list) is True


def test_get_data_from_api_with_invalid_endpoint_raises_exception():
    with pytest.raises(Exception):
        api._get_data_from_api(api_endpoint=INVALID_API_ENDPOINT)


def test_get_stops_for_route_and_direction_with_valid_input_returns_list():
    stops = api.get_stops_for_route_and_direction(route_id=VALID_ROUTE_ID, direction_id=VALID_DIRECTION_ID)
    assert isinstance(stops, list)


def  test_get_stops_for_route_and_direction_with_invalid_inputs_raises_exception():
    with pytest.raises(Exception):
        api.get_stops_for_route_and_direction(route_id=INVALID_ROUTE_ID, direction_id=VALID_DIRECTION_ID)
    
    with pytest.raises(Exception):
        api.get_stops_for_route_and_direction(route_id=VALID_ROUTE_ID, direction_id=INVALID_DIRECTION_ID)


    with pytest.raises(Exception):
        api.get_stops_for_route_and_direction(route_id=INVALID_ROUTE_ID, direction_id=INVALID_DIRECTION_ID)



def test_get_next_departure_with_valid_input_returns_dict():
    departures = api.get_departures(route_id=VALID_ROUTE_ID, direction_id=VALID_DIRECTION_ID, place_code=VALID_PLACE_CODE)
    assert isinstance(departures, list)


def test_get_next_departure_with_invalid_inputs_raises_exception():
    with pytest.raises(Exception):
        api.get_departures(route_id=INVALID_ROUTE_ID, direction_id=VALID_DIRECTION_ID, place_code=VALID_PLACE_CODE)
    
    with pytest.raises(Exception):
        api.get_departures(route_id=VALID_ROUTE_ID, direction_id=VALID_DIRECTION_ID, place_code=INVALID_PLACE_CODE)


    with pytest.raises(Exception):
        api.get_departures(route_id=VALID_ROUTE_ID, direction_id=INVALID_DIRECTION_ID, place_code=VALID_PLACE_CODE)


    with pytest.raises(Exception):
        api.get_departures(route_id=INVALID_ROUTE_ID, direction_id=INVALID_DIRECTION_ID, place_code=INVALID_PLACE_CODE)
