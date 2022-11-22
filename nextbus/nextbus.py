import time

from userinput import userinput
from helpers import loghelpers, directionhelpers, datahelpers, timehelpers
from api import api

ROUTE_KEYS = ["Description", "ProviderID", "Route"]
STOP_KEYS = ["Text", "Value"]

if __name__ == "__main__":
    # logger = loghelpers.init_logger()

    input_route, input_stop, input_direction = userinput.get_user_input()

    start_time = time.perf_counter()

    direction_int = directionhelpers.cardinal_direction_to_int(
        direction=input_direction)

    routes_list = api.get_routes()
    routes_lookup = datahelpers.parse_list_to_lookup(
        entries=routes_list, essential_keys=ROUTE_KEYS, key_name="Description")
    route_id = datahelpers.get_entry_id_from_input(
        entry_name=input_route, lookup=routes_lookup, return_key="Route")

    if route_id is not None:
        stops_list = api.get_stops_for_route_and_direction(
            route=route_id, direction=direction_int)

        if stops_list is not None:
            stops_lookup = datahelpers.parse_list_to_lookup(
                entries=stops_list, essential_keys=STOP_KEYS, key_name="Text")

            stop_id = datahelpers.get_entry_id_from_input(
                entry_name=input_stop, lookup=stops_lookup, return_key="Value")

            if stop_id is not None:
                next_departure = api.get_next_departure(
                    route=route_id, stop=stop_id, direction=direction_int)

                if next_departure is not None:
                    time_to_next_departure = timehelpers.get_time_to_next_departure(
                        next_departure)
                    print(time_to_next_departure)
                    end_time = time.perf_counter()
                    elapsed_run_time = end_time - start_time
                    loghelpers.log_success(start_time=start_time, message=f"input:{input_route} {input_stop} {input_direction}")

            else:
                error_message = f"Could not find stop on route {input_route} matching {input_stop}"
                loghelpers.log_failure(start_time=start_time, message=f"input:{input_route} {input_stop} {input_direction} errormessage:{error_message}")
                print(error_message)
                    

        else:
            error_message =  f"Could not find stops on route {route_id} going direction {input_direction}"
            loghelpers.log_failure(start_time=start_time, message=f"input:{input_route} {input_stop} {input_direction} errormessage:{error_message}")
            print(error_message)

    else:
        error_message = f"Could not find route {input_route}"
        loghelpers.log_failure(start_time=start_time, message=f"input:{input_route} {input_stop} {input_direction} errormessage:{error_message}")
        print(error_message)
