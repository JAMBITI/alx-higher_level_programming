#!/usr/bin/python3
'''From JSON string to Object'''
import json


def from_json_string(my_str):
    ''' A function that returns an object
    From JSON string to Object'''
    return json.loads(my_str)
