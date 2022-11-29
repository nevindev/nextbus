import pytest

from helpers import datahelpers

ROUTE_KEYS = ["route_label", "agency_id", "route_id"]

VALID_ROUTES_LIST = [
  {
    "route_id": "901",
    "agency_id": 0,
    "route_label": "METRO Blue Line"
  },
  {
    "route_id": "902",
    "agency_id": 0,
    "route_label": "METRO Green Line"
  },
  {
    "route_id": "904",
    "agency_id": 0,
    "route_label": "METRO Orange Line"
  },
  {
    "route_id": "425",
    "agency_id": 3,
    "route_label": "Orange Link"
  },
  {
    "route_id": "903",
    "agency_id": 0,
    "route_label": "METRO Red Line"
  },
  {
    "route_id": "921",
    "agency_id": 0,
    "route_label": "METRO A Line"
  },
  {
    "route_id": "923",
    "agency_id": 0,
    "route_label": "METRO C Line"
  }
]

INVALID_ROUTES_LIST = [
    # missing "route_label" key
    {"agency_id": "0", "route_id": "902"},
    # missing "route_id" key
    {"other_key": "METRO Orange Line", "agency_id": "0"},
    # changed "route_label" key to "other_key"
    {"other_key": "Orange Link", "agency_id": "3", "route_id": "425"},
    # changed "route_label" key to "other_key"
    {"route_label": "METRO A Line", "agency_id": "0", "other_key": "921"}
]

EMPTY_ROUTES_LIST = []


def test_parse_routes_to_lookup_with_valid_list_returns_dict():
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="route_label")

    assert isinstance(routes_lookup, dict) is True

    assert len(routes_lookup) == len(VALID_ROUTES_LIST)

    for key, entry in routes_lookup.items():
        assert key == datahelpers._normalize(entry["route_label"])


def test_parse_routes_to_lookup_with_empty_list_returns_empty_dict():
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=EMPTY_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="route_label")

    assert isinstance(routes_lookup, dict)

    assert len(routes_lookup) == 0


def test_parse_routes_to_lookup_with_invalid_list_skips_invalid_entries():

    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=INVALID_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="route_label")

    assert isinstance(routes_lookup, dict)

    for item in INVALID_ROUTES_LIST:
        if "other_key" in item:
            assert item["other_key"] not in routes_lookup

    # Assert that every bad entry should be excluded from the lookup dictionary
    for bad_entry in INVALID_ROUTES_LIST:
        assert bad_entry not in routes_lookup.values()


def test_get_entry_id_from_input_with_valid_entry_key_returns_entry_id():
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="route_label")

    route_name = "METRO Blue Line"

    route_id = datahelpers.get_entry_id_from_lookup(
        entry_key=route_name, lookup=routes_lookup, return_key="route_id")

    assert route_id == "901"


def test_get_entry_id_from_input_with_invalid_entry_raises_exception():
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=VALID_ROUTES_LIST, essential_keys=ROUTE_KEYS, key_name="route_label")

    route_name = "Nonexistant Metro Line"
    
    with pytest.raises(LookupError):
        datahelpers.get_entry_id_from_lookup(
            entry_key=route_name, lookup=routes_lookup, return_key="route_id")


def test_search_list_for_entry_with_valid_entry_returns_desired_value():
    value_from_route_id_search = datahelpers.search_list_for_entry(
      entry_value="901", entries=VALID_ROUTES_LIST, return_key="route_id")

    value_from_route_label_search =  datahelpers.search_list_for_entry(
      entry_value="  MET RO Blu e  Li ne ", entries=VALID_ROUTES_LIST, return_key="route_id")

    assert value_from_route_id_search == value_from_route_label_search
    assert isinstance(value_from_route_id_search, str)
    assert isinstance(value_from_route_label_search, str)

    assert VALID_ROUTES_LIST[0]["route_id"] == value_from_route_label_search and \
    VALID_ROUTES_LIST[0]["route_id"] == value_from_route_id_search


def test_search_list_for_entry_with_invalid_entry_returns_none():
  invalid_value_search = datahelpers.search_list_for_entry(
    entry_value="garbage", entries=VALID_ROUTES_LIST, return_key="route_id")
  
  assert invalid_value_search is None


def test_search_list_for_entry_with_valid_entry_and_invalid_return_key_returns_none():
  invalid_return_key_search = datahelpers.search_list_for_entry(
      entry_value="901", entries=VALID_ROUTES_LIST, return_key="garbage")
    
  assert invalid_return_key_search is None