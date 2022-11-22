# import pytest

from helpers import directionhelpers

valid_directions = ['north', 'SOUTH', '   easT   ', 'west  ']
invalid_directions = ['foo', 'bar']


def test_cardinal_direction_to_int_with_valid_input_returns_int():
    for valid_direction in valid_directions:
        direction_int = directionhelpers.cardinal_direction_to_int(
            direction=valid_direction)
        assert direction_int > 0 and direction_int < 5


def test_cardinal_direction_to_int_with_invalid_input_returns_negative():
    for invalid_direction in invalid_directions:
        direction_int = directionhelpers.cardinal_direction_to_int(
            direction=invalid_direction)
        assert direction_int == -1
