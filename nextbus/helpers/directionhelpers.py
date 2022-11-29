from typing import Union

HEADINGS = {"north": "northbound", "south": "southbound", "east": "eastbound", "west": "westbound"}


def _cardinal_direction_to_heading(direction: str) -> Union[str, None]:
    normalized_direction = direction.lower().strip().replace(" ", "")
    return HEADINGS.get(normalized_direction, None)


def get_direction_id_from_data(direction: str, direction_data: list) -> Union[int, None]:
    """
    Given a direction string and dictionary of route directions from the API /directions/{route_id} endpoint,
    returns the corresponding integer for the associated 'heading' value for the direction key

    A route only travels opposite cardinal directions: Northbound and Southbound or Eastbound and Westbound.


    Keyword arguments:

    direction           --      string value of a cardinal direction (north, south, east, west)

    direction_data      --      dictionary containing the headings associated with the directions
                                a route travels. Provided from the API.

                                [
                                    {
                                        "direction_id": 0,
                                        "direction_name": "string"
                                    },
                                    {
                                        "direction_id": 1,
                                        "direction_name": "string
                                    },
                                ]

    Returns:

    -   Integer value of the 'direction_id' corresponding with the 'direction_name' associated
        with the provided 'direction' argument.
    
    -   NoneType if the heading retrieved from the 'direction' argument does not exist in the
        direction data provided by the API for the input route.

    """
    heading = _cardinal_direction_to_heading(direction=direction)
    for entry in direction_data:
        if heading in entry["direction_name"].lower():
            return dict(entry).get("direction_id", None)
