
def _normalize(value: str) -> str:
    normalized_string = str(value).replace(" ", "").lower()
    return normalized_string


def parse_list_to_lookup(entries: list, essential_keys: list, key_name: str) -> dict:
    """
    Because most of the data returned by the API is a list (routes, stops, departures), 
    search time complexity can be improved by constructing a dictionary from the lists, using
    a desired value in said list as a key, which can be used in future lookups.
    Because the names of the routes, stops, etc are more than likely unique in the dataset,
    they are good candidates for keys.

    Keyword arguments:

    entries             --      a list object of the data retrieved from the API

    essential_keys      --      the list of keys defined by the API for each record in a dataset.
                                Before entry into the 'lookup' dictionary, each key is verified to exist
                                on each record so that the 'lookup' dictionary being created does not have holes.
    
    key_name            --      the key name that corresponds to the desired value in the 'entries' list, which will
                                be used as the primary key in the lookup dictionary that is created.
    
    Logic:

    Iterates over every item in the provided 'entries' list, verifying the record has all the keys that are promised by the API.
    For each item, the value at the 'key name' key is _normalized() to cast the type to a string, remove all whitespace and lowercase it.
    The string normalization is done because certain records in the API have inconsistent spacing.
    A new key value is added to the 'lookup' dictionary, the normalized string as the key and the entry from the list as the value.

    Returns:

    the 'lookup' dictionary object.
    """
    lookup = {}
    for entry in entries:
        if all(key in entry for key in essential_keys):
            lookup.update({_normalize(value=entry[str(key_name)]): entry})
    return lookup


def get_entry_id_from_lookup(entry_key: str, lookup: dict, return_key: str):
    """
    Taking advantage of the O(1) time complexity for a dictionary lookup by key,
    given an entry key (which is normalized, due to the same normalizing that occurs
    in the dictionary construction in the 'parse_list_to_lookup() function), return
    the value of the specified return_key for that entry.

    Keyword arguments:

    entry_key   --      the 'primary key' that will be used for looking up associated
                        entries in the provided 'lookup' dictionary.

    lookup      --      the dictionary object that contains the data to be searched.
    
    return_key  --      the key for the value to be returned from a matching entry
                        in the 'lookup' dictionary.

    Returns:

    The value for the given 'return_key' key on the object in the 'lookup' dictionary at the 'entry_key' key.

    Exceptions:

    LookupError raised if no object is found in the dictionary at the given 'entry_key'

    """
    try:
        return lookup[_normalize(value=entry_key)][str(return_key)]
    except LookupError as exc:
        print(f"Could not find {entry_key}")
        error_message = f"key {exc} could not be found in lookup dictionary"
        raise LookupError(f"{error_message}") from exc


def search_list_for_entry(entry_value: str, entries: list, return_key: str):
    """
    Rather than using a dictionary for all lookups, which requires the provided key to match an entry,
    it can be advantageous (albeit worst-case slower) to traverse a list of dictionaries and check if any
    of the values match the provided entry value.

    This allows a user to enter a "common" name for a bus route (i.e. METRO Blue Line) OR the corresponding 
    route number (i.e. 901), and since both are captured in a dictionary item in the list of entries,
    either input will return a valid match.

    The tradeoff between search speed and flexibility may be worth it, because users are not guaranteed
    to only enter the "common" names for routes, etc.

    The input and values for each dictionary in the list are normalized, because the API data has inconsistencies
    with spacing for certain records.

    Keyword arguments:

    entry_value     --      the input to be searched for in the list

    entries         --      the list of records returned by the API

    return_key      --      the key associated with the desired value to be returned 
                            from the matching dictionary entry in the list.
    
    Returns:

    -   the value of the requested key if there is a matching entry in the list.

    -   NoneType if there is a match, but the return_key does not exist in the dictionary.

    """
    for entry in entries:
        if _normalize(value=entry_value) in {_normalize(value=v) for v in entry.values()}:
            return dict(entry).get(return_key, None)

    return None

