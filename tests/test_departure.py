import pytest
from helpers import timehelpers


# with open('../tests/test_data/valid_departures.json', 'r') as valid_departures_data:
#     VALID_DEPARTURES_LIST = json.load(valid_departures_data)

# with open('../tests/test_data/invalid_departures.json', 'r') as invalid_departures_data:
#     INVALID_DEPARTURES_LIST = json.load(invalid_departures_data)

VALID_DEPARTURES_LIST = [
    {
      "actual": "false",
      "trip_id": "22168531-AUG22-MVS-UM-Weekday-01",
      "stop_id": 54035,
      "departure_text": "8:30",
      "departure_time": 1669645800,
      "description": "4th Street / Circulator",
      "route_id": "123",
      "route_short_name": "123",
      "direction_id": 0,
      "direction_text": "EB",
      "schedule_relationship": "Scheduled"
    },
    {
      "actual": "false",
      "trip_id": "22168532-AUG22-MVS-UM-Weekday-01",
      "stop_id": 54035,
      "departure_text": "8:40",
      "departure_time": 1669646400,
      "description": "4th Street / Circulator",
      "route_id": "123",
      "route_short_name": "123",
      "direction_id": 0,
      "direction_text": "EB",
      "schedule_relationship": "Scheduled"
    },
    {
      "actual": "false",
      "trip_id": "22168574-AUG22-MVS-UM-Weekday-01",
      "stop_id": 54035,
      "departure_text": "8:50",
      "departure_time": 1669647000,
      "description": "4th Street / Circulator",
      "route_id": "123",
      "route_short_name": "123",
      "direction_id": 0,
      "direction_text": "EB",
      "schedule_relationship": "Scheduled"
    }
]

INVALID_DEPARTURES_LIST = [
    {
      "actual": "false",
      "trip_id": "22168531-AUG22-MVS-UM-Weekday-01",
      "stop_id": 54035,
      "departure_text": "8:30",
      "other_key": 1669645800,
      "description": "4th Street / Circulator",
      "route_id": "123",
      "route_short_name": "123",
      "direction_id": 0,
      "direction_text": "EB",
      "schedule_relationship": "Scheduled"
    },
    {
      "actual": "false",
      "trip_id": "22168532-AUG22-MVS-UM-Weekday-01",
      "stop_id": 54035,
      "departure_text": "8:40",
      "departure_time": "\/Date(1669072620000-0600)\/",
      "description": "4th Street / Circulator",
      "route_id": "123",
      "route_short_name": "123",
      "direction_id": 0,
      "direction_text": "EB",
      "schedule_relationship": "Scheduled"
    },
    {
      "actual": "false",
      "trip_id": "22168574-AUG22-MVS-UM-Weekday-01",
      "stop_id": 54035,
      "departure_text": "8:50",
      "description": "4th Street / Circulator",
      "route_id": "123",
      "route_short_name": "123",
      "direction_id": 0,
      "direction_text": "EB",
      "schedule_relationship": "Scheduled"
    },
]

EMPTY_DEPARTURES_LIST = []


def test_get_time_to_next_departure_with_valid_departure_returns_string():
    for departure in VALID_DEPARTURES_LIST:
        time_to_next_departure = timehelpers.v2_get_time_to_next_departure(next_departure=departure)
        assert isinstance(time_to_next_departure, str)


def test_get_time_to_next_departure_with_invalid_departure_raises_exception():
    for invalid_departure in INVALID_DEPARTURES_LIST:
      with pytest.raises(Exception):
        timehelpers.v2_get_time_to_next_departure(next_departure=invalid_departure)