import datetime
import re
from typing import Tuple, Union


def _parse_timestring(timestring: str) -> Union[Tuple[datetime.datetime, datetime.timezone], Tuple[None, None]]:
    """
    Because the API DepartureTime has a non-ISO-8601 format /Date(1668802680000-0600)/,
    it needs to be parsed into a timestamp component and a timezone offset component
    and converted into a Python datetime object.

    Keyword arguments:

    timestring      --      The value of DepartureTime from the API response object.
                            Takes the form /Date(1668802680000-0600)/

    Logic:

    Replaces the word "Date" with nothing,
    and strips the slashes and parantheses from the timestring.

    Uses a regex to break the string into groups corresponding
    to the milliseconds, timezone offset direction and timezone magnitude.

    Creates a timezone object from the parsed timezone values

    Creates a datetime from the timestamp
    (divided by 1000, since Python uses seconds since the epoch)
    and timezone object.

    Returns:

    Created datetime object

    Created timezone object

    """
    time = str(timestring).strip(
        "/").replace('Date', '').lstrip("(").rstrip(")")
    try:
        timestamp, sign, hours, minutes = re.match(
            '(\\d+)([+\\-]?)(\\d{2})(\\d{2})', time).groups()
    except AttributeError:
        return None, None
    sign = -1 if sign == '-' else 1

    timezone = datetime.timezone(
        sign * datetime.timedelta(hours=int(hours), minutes=int(minutes)))

    date = datetime.datetime.fromtimestamp(int(timestamp) / 1e3, tz=timezone)

    return date, timezone


def _delta_time_from_now(date: datetime.datetime, timezone=None) -> datetime.timedelta:
    """
    Calculates the difference in time from now until the next departure

    Keyword arguments:

    date        --      datetime object of the next departure

    timezone    --      timezone object corresponding to the date 
                        (the API data is for Minnesota UTC-0600)
                        Defaults to None, so no timezone is used 
                        for the caller unless explicitly provided.

    Returns:

    datetime.timedelta object


    """
    if date is None:
        return None

    delta_time = date - datetime.datetime.now(tz=timezone)
    return delta_time


def get_time_to_next_departure(next_departure: dict) -> Union[str, None]:
    """
    Keyword arguments:
    next_departure      --      data dictionary containing one departure entry retrieved from the API

    Logic:

    Attempts to access the value of the DepartureTime key in the next_departure dictionary.

    DepartureTime takes the form of "/Date(1668802680000-0600)/", which is not an ISO-8601 standard format

    The DepartureTime value is parsed into a Python native datetime type for ease-of-use.

    The current time (as a datetime) is subtracted from the bus departure datetime.
    This operation results in a timedelta that can be parsed and formatted into a MM:SS string 
    
    Returns:
    None if the DepartureTime key does not exist in the dictionary

    String containing the formatted time until next departure 
    if DepartureTime is a valid key and the value can be parsed.
    """

    try:
        departure_time = next_departure['DepartureTime']

        departure_date, timezone = _parse_timestring(departure_time)

        delta_time = _delta_time_from_now(
            date=departure_date, timezone=timezone)
        
        if not isinstance(delta_time, datetime.timedelta):
            return None
        
        return f"{delta_time.seconds / 60:.0f} minutes {delta_time.seconds % 60} seconds"

    except KeyError:
        return None
