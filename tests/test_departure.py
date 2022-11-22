import json
from pathlib import Path
from helpers import timehelpers


with open('../tests/test_data/valid_departures.json', 'r') as valid_departures_data:
    VALID_DEPARTURES_LIST = json.load(valid_departures_data)

with open('../tests/test_data/invalid_departures.json', 'r') as invalid_departures_data:
    INVALID_DEPARTURES_LIST = json.load(invalid_departures_data)

EMPTY_DEPARTURES_LIST = []


def test_get_time_to_next_departure_with_valid_departure_returns_string():
    for departure in VALID_DEPARTURES_LIST:
        time_to_next_departure = timehelpers.get_time_to_next_departure(next_departure=departure)
        assert isinstance(time_to_next_departure, str)

def test_get_time_to_next_departure_with_invalid_departure_returns_none():
    for invalid_departure in INVALID_DEPARTURES_LIST:
        time_to_next_departure = timehelpers.get_time_to_next_departure(next_departure=invalid_departure)
        assert time_to_next_departure is None