from typing import Union


def parse_list_to_lookup(entries: list, essential_keys: list, key_name: str) -> dict:
    lookup = {}
    for entry in entries:
        if all(key in entry for key in essential_keys):
            lookup.update({entry[str(key_name)].lower(): entry})

    return lookup


def get_entry_id_from_input(entry_name: str, lookup: dict, return_key: str) -> Union[str, None]:
    try:
        return lookup[entry_name.lower()][str(return_key)]
    except KeyError:
        return None