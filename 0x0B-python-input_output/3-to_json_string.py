#!/usr/bin/python3
"""
contain the JSON string
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.umps(my_obj)
cat > 4-from_jsonstring.py
#!/usr/bin/python3
"""
contains the json str function
"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
