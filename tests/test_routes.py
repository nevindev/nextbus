from helpers import datahelpers

ROUTE_KEYS = ["Description", "ProviderID", "Route"]

VALID_ROUTES_LIST = [
    {"Description": "METRO Blue Line", "ProviderID": "0", "Route": "901"},
    {"Description": "METRO Green Line", "ProviderID": "0", "Route": "902"},
    {"Description": "METRO Orange Line", "ProviderID": "0", "Route": "904"},
    {"Description": "Orange Link", "ProviderID": "3", "Route": "425"},
    {"Description": "METRO Red Line", "ProviderID": "0", "Route": "903"},
    {"Description": "METRO A Line", "ProviderID": "0", "Route": "921"},
    {"Description": "METRO C Line", "ProviderID": "0", "Route": "923"},
    {"Description": "Northstar Commuter Rail", "ProviderID": "0", "Route": "888"},
    {"Description": "Northstar Link", "ProviderID": "15", "Route": "887"},
    {"Description": "Airport Shuttle", "ProviderID": "10", "Route": "906"}
]

INVALID_ROUTES_LIST = [
    # missing "Description" key
    {"ProviderID": "0", "Route": "902"},
    # missing "Route" key
    {"OtherKeyName": "METRO Orange Line", "ProviderID": "0"},
    # changed "Description" key to "OtherKeyName"
    {"OtherKeyName": "Orange Link", "ProviderID": "3", "Route": "425"},
    # changed "Route" key to "OtherKeyName"
    {"Description": "METRO A Line", "ProviderID": "0", "OtherKeyName": "921"}
]

EMPTY_ROUTES_LIST = []


def test_parse_routes_to_lookup_with_valid_list_returns_dict():
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="Description")

    assert isinstance(routes_lookup, dict) is True

    assert len(routes_lookup) == len(VALID_ROUTES_LIST)

    for key, entry in routes_lookup.items():
        assert key == entry["Description"].lower()

        for value in entry:
            assert value in ROUTE_KEYS


def test_parse_routes_to_lookup_with_empty_list_returns_empty_dict():
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=EMPTY_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="Description")

    assert isinstance(routes_lookup, dict)

    assert len(routes_lookup) == 0


def test_parse_routes_to_lookup_with_invalid_list_skips_invalid_entries():

    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=INVALID_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="Description")

    assert isinstance(routes_lookup, dict)

    for item in INVALID_ROUTES_LIST:
        if "OtherKeyName" in item:
            assert item["OtherKeyName"] not in routes_lookup

    # Assert that every bad entry should be excluded from the lookup dictionary
    for bad_entry in INVALID_ROUTES_LIST:
        assert bad_entry not in routes_lookup.values()


def test_get_entry_id_from_input_with_valid_entry_name_returns_entry_id():
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="Description")

    route_name = "METRO Blue Line"

    route_id = datahelpers.get_entry_id_from_input(
        entry_name=route_name, lookup=routes_lookup, return_key="Route")

    assert route_id == "901"


def test_get_entry_id_from_input_with_invalid_entry_name_returns_none():
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="Description")

    route_name = "Nonexistant Metro Line"

    route_id = datahelpers.get_entry_id_from_input(
        entry_name=route_name, lookup=routes_lookup, return_key="Route")

    assert route_id is None
