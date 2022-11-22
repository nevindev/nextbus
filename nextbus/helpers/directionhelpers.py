def cardinal_direction_to_int(direction: str) -> int:
    directions = {"south": 1, "east": 2, "west": 4, "north": 4}
    return directions.get(direction.lower().strip(), -1)
