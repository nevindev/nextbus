import time

from userinput import userinput
from helpers import loghelpers, directionhelpers, datahelpers, timehelpers
from api import api

ROUTE_KEYS = ["route_label", "agency_id", "route_id"]
STOP_KEYS = ["place_code", "description"]


if __name__ == "__main__":

    try:

        # User Input
        input_route, input_stop, input_direction = userinput.get_user_input()

        start_time = time.perf_counter()

        # Fetch all routes and parse data
        routes_list = api.get_routes()
        route_id = datahelpers.search_list_for_entry(entry_value=input_route, entries=routes_list, return_key="route_id")
        if route_id is None:
            print(f"Could not find a route matching {input_route}.")
            raise SystemExit()
        
        # Fetch valid directions for given route and parse data
        route_directions = api.get_directions_for_route(route_id=route_id)
        direction_id = directionhelpers.get_direction_id_from_data(direction=input_direction, direction_data=route_directions)
        if direction_id is None:
            valid_directions = "/".join(str(val["direction_name"]) for val in route_directions)
            print(f"{input_route} (Route {route_id}) travels {valid_directions}")
            raise SystemExit()

        # Fetch all stops for given route going given direction and parse data
        stops_list = api.get_stops_for_route_and_direction(route_id=route_id, direction_id=direction_id)
        stops_lookup = datahelpers.parse_list_to_lookup(
            entries=stops_list, essential_keys=STOP_KEYS, key_name="description")
        place_code = datahelpers.get_entry_id_from_lookup(
            entry_key=input_stop, lookup=stops_lookup, return_key="place_code")

        # Fetch departure data from given route going direction from stop
        departures = api.get_departures(
            route_id=route_id, direction_id=direction_id, place_code=place_code)

        # Calculate delta time from departure data
        if len(departures) > 0:
            time_to_next_departure = timehelpers.v2_get_time_to_next_departure(departures[0])
            print(time_to_next_departure)
        else:
            print("No more departures scheduled for the day.")

        # End timer and log information about run
        end_time = time.perf_counter()
        loghelpers.log_success(start_time=start_time, message=f"input:--route {input_route} --stop {input_stop} -direction {input_direction}")

    except (LookupError, ValueError, TypeError) as e:
        end_time = time.perf_counter()
        loghelpers.log_failure(start_time=start_time, message=f"input:--route {input_route} --stop {input_stop} -direction {input_direction} error:{str(type(e).__name__)} {list(e.args)}")