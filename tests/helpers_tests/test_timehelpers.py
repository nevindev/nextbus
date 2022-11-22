import datetime

from helpers import timehelpers

VALID_TIMESTRING = "/Date(1668802680000-0600)/"
VALID_DATETIME = datetime.datetime(1970, 1, 1, 0, 0, 0, 0, tzinfo=None)

DIFFERENT_TIMESTRING = "2022-11-22T15:50-06:00"

EMPTY_TIMESTRING = ""


def test_parse_timestring_with_valid_input_returns_datetime_and_timezone():

    date, timezone = timehelpers._parse_timestring(timestring=VALID_TIMESTRING)

    assert isinstance(date, datetime.datetime) is True
    assert isinstance(timezone, datetime.timezone) is True


def test_parse_timestring_with_invalid_input_returns_none():
    different_date, different_timezone = timehelpers._parse_timestring(timestring=DIFFERENT_TIMESTRING)

    assert different_date is None
    assert different_timezone is None

    empty_date, empty_timezone = timehelpers._parse_timestring(timestring=EMPTY_TIMESTRING)

    assert empty_date is None
    assert empty_timezone is None

def test_delta_time_from_now_with_valid_datetimes_returns_timedelta():
    delta_time = timehelpers._delta_time_from_now(
        date=VALID_DATETIME, timezone=None)

    assert isinstance(delta_time, datetime.timedelta) is True
