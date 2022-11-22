from helpers import datahelpers

STOP_KEYS = ["Text", "Value"]

VALID_STOPS_LIST = [
    {"Text": "Target Field Station Platform 2", "Value": "TF2"},
    {"Text": "Target Field Station Platform 1", "Value": "TF1"},
    {"Text": "Warehouse District\/ Hennepin Ave Station", "Value": "WARE"},
    {"Text": "Nicollet Mall Station", "Value": "5SNI"},
    {"Text": "Government Plaza Station", "Value": "GOVT"},
    {"Text": "U.S. Bank Stadium Station", "Value": "USBA"},
    {"Text": "Cedar-Riverside Station", "Value": "CDRV"}
]

INVALID_STOPS_LIST = [
    # missing "Text" key
    {"Value": "GOVT"},
    # missing "Value" key
    {"Text": "Target Field Station Platform 1"},
    # changed "Text" key to "OtherKeyName"
    {"OtherKeyName": "Warehouse District\/ Hennepin Ave Station", "Value": "WARE"},
    # changed "Value" key to "OtherKeyName"
    {"Text": "Nicollet Mall Station", "OtherKeyName": "5SNI"}
]

EMPTY_STOPS_LIST = []


def test_parse_stops_to_lookup_with_valid_list_returns_dict():
    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_STOPS_LIST, essential_keys=STOP_KEYS, key_name="Text")

    assert isinstance(stops_lookup, dict) is True

    assert len(stops_lookup) == len(VALID_STOPS_LIST)

    for key, entry in stops_lookup.items():
        assert key == entry['Text'].lower()

        for value in entry:
            assert value in STOP_KEYS


def test_parse_stops_to_lookup_with_empty_list_returns_empty_dict():
    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=EMPTY_STOPS_LIST, essential_keys=STOP_KEYS, key_name="Text")

    assert isinstance(stops_lookup, dict)

    assert len(stops_lookup) == 0


def test_parse_stops_to_lookup_with_invalid_list_skips_invalid_entries():

    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=INVALID_STOPS_LIST, essential_keys=STOP_KEYS, key_name="Text")

    assert isinstance(stops_lookup, dict)

    for item in INVALID_STOPS_LIST:
        if "OtherKeyName" in item:
            assert item["OtherKeyName"] not in stops_lookup

    # Assert that every bad entry should be excluded from the lookup dictionary
    for bad_entry in INVALID_STOPS_LIST:
        assert bad_entry not in stops_lookup.values()


def test_get_entry_id_from_input_with_valid_entry_name_returns_entry_id():
    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_STOPS_LIST, essential_keys=STOP_KEYS, key_name="Text")

    stop_name = "Target Field Station Platform 2"

    stop_id = datahelpers.get_entry_id_from_input(
        entry_name=stop_name, lookup=stops_lookup, return_key="Value")

    assert stop_id == "TF2"


def test_get_entry_id_from_input_with_invalid_entry_name_returns_none():
    stops_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_STOPS_LIST, essential_keys=STOP_KEYS, key_name="Text")

    stop_name = "Nonexistant Metro Line Stop"

    stop_id = datahelpers.get_entry_id_from_input(
        entry_name=stop_name, lookup=stops_lookup, return_key="Value")

    assert stop_id is None
