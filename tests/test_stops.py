import pytest
from helpers import datahelpers

STOP_KEYS = ["description", "place_code"]

VALID_STOPS_LIST = [
    {"description": "Target Field Station Platform 2", "place_code": "TF2"},
    {"description": "Target Field Station Platform 1", "place_code": "TF1"},
    {"description": "Warehouse District/ Hennepin Ave Station", "place_code": "WARE"},
    {"description": "Nicollet Mall Station", "place_code": "5SNI"},
    {"description": "Government Plaza Station", "place_code": "GOVT"},
    {"description": "U.S. Bank Stadium Station", "place_code": "USBA"},
    {"description": "Cedar-Riverside Station", "place_code": "CDRV"},
    {"place_code": "19RO", "description": "19th Ave and 3rd St - Leave"},
    {"place_code": "19RP", "description": "19th  Ave and 3rd St - Arrive"}
]

INVALID_STOPS_LIST = [
    # missing "description" key
    {"place_code": "GOVT"},
    # missing "place_code" key
    {"description": "Target Field Station Platform 1"},
    # changed "description" key to "other_key"
    {"other_key": "Warehouse District/ Hennepin Ave Station", "place_code": "WARE"},
    # changed "place_code" key to "other_key"
    {"description": "Nicollet Mall Station", "other_key": "5SNI"}
]

EMPTY_STOPS_LIST = []


def test_parse_stops_to_lookup_with_valid_list_returns_dict():
    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_STOPS_LIST, essential_keys=STOP_KEYS, key_name="description")

    assert isinstance(stops_lookup, dict) is True

    assert len(stops_lookup) == len(VALID_STOPS_LIST)

    for key, entry in stops_lookup.items():
        assert key == datahelpers._normalize(entry['description'])

        for value in entry:
            assert value in STOP_KEYS


def test_parse_stops_to_lookup_with_empty_list_returns_empty_dict():
    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=EMPTY_STOPS_LIST, essential_keys=STOP_KEYS, key_name="description")

    assert isinstance(stops_lookup, dict)

    assert len(stops_lookup) == 0


def test_parse_stops_to_lookup_with_invalid_list_skips_invalid_entries():

    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=INVALID_STOPS_LIST, essential_keys=STOP_KEYS, key_name="description")

    assert isinstance(stops_lookup, dict)

    for item in INVALID_STOPS_LIST:
        if "other_key" in item:
            assert item["other_key"] not in stops_lookup

    # Assert that every bad entry should be excluded from the lookup dictionary
    for bad_entry in INVALID_STOPS_LIST:
        assert bad_entry not in stops_lookup.values()


def test_get_entry_id_from_input_with_valid_entry_key_returns_entry_id():
    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_STOPS_LIST, essential_keys=STOP_KEYS, key_name="description")

    stop_name = "Target Field Station Platform 2"

    stop_id = datahelpers.get_entry_id_from_lookup(
        entry_key=stop_name, lookup=stops_lookup, return_key="place_code")

    assert stop_id == "TF2"


def test_get_entry_id_from_input_with_invalid_entry_key_raises_exception():
    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_STOPS_LIST, essential_keys=STOP_KEYS, key_name="description")

    stop_name = "Nonexistant Metro Line Stop"

    with pytest.raises(LookupError):
        datahelpers.get_entry_id_from_lookup(
            entry_key=stop_name, lookup=stops_lookup, return_key="place_code")