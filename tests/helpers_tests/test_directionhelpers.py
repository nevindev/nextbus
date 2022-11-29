import pytest
from helpers import directionhelpers

VALID_DIRECTIONS = ['north', 'SOUTH', '   easT   ', 'west  ']
INVALID_DIRECTIONS = ['foo', 'bar']

VALID_DIRECTION_DATA_E_W = [
  {
    "direction_id": 0,
    "direction_name": "Eastbound"
  },
  {
    "direction_id": 1,
    "direction_name": "Westbound"
  }
]

VALID_DIRECTION_DATA_N_S = [
  {
    "direction_id": 0,
    "direction_name": "Northbound"
  },
  {
    "direction_id": 1,
    "direction_name": "Southbound"
  }
]


def test_cardinal_direction_to_heading_with_valid_input_returns_string():
    for valid_direction in VALID_DIRECTIONS:
        heading = directionhelpers._cardinal_direction_to_heading(direction=valid_direction)
        assert isinstance(heading, str)
        assert f"{valid_direction.lower().strip()}bound" == heading


def test_cardinal_direction_to_heading_with_invalid_input_returns_none():
    for invalid_direction in INVALID_DIRECTIONS:
        heading = directionhelpers._cardinal_direction_to_heading(direction=invalid_direction)
        assert heading is None


def test_get_direction_id_from_data_with_valid_input_returns_int():
    for valid_direction in VALID_DIRECTIONS[0:1]:
        direction_id = directionhelpers.get_direction_id_from_data(direction=valid_direction, direction_data =VALID_DIRECTION_DATA_N_S)
        assert isinstance(direction_id, int)
    
    for valid_direction in VALID_DIRECTIONS[2:3]:
        direction_id = directionhelpers.get_direction_id_from_data(direction=valid_direction, direction_data=VALID_DIRECTION_DATA_E_W)
        assert isinstance(direction_id, int)


def test_get_direction_id_from_data_with_invalid_input_returns_none():
    for invalid_direction in INVALID_DIRECTIONS:
        with pytest.raises(Exception):
            directionhelpers.get_direction_id_from_data(direction=invalid_direction, direction_data=VALID_DIRECTION_DATA_N_S)
        
        with pytest.raises(Exception):
            directionhelpers.get_direction_id_from_data(direction=invalid_direction, direction_data=VALID_DIRECTION_DATA_E_W)