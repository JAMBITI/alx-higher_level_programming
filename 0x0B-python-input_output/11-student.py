#!/usr/bin/python3

"""
This module defines the Student class
"""


class Student:


"""
The Student class represents a student
"""


def __init__(self, first_name, last_name, age):


"""
Initializes a new Student instance

Args:
first_name (str): The first name of the student
last_name (str): The last name of the student
age (int): The age of the student
"""
self.first_name = first_name
self.last_name = last_name
self.age = age


def to_json(self, attrs=None):


"""
Retrieves a dictionary representation of a Student instance

Args:
attrs (list of str): A list of attributes to include in the dictionary

Returns:
dict: A dictionary containing the selected attributes of the Student
"""
student_dict = {}
if isinstance(attrs, list):
for attr in attrs:
if isinstance(attr, str) and hasattr(self, attr):
student_dict[attr] = getattr(self, attr)
return student_dict

return self.__dict__

def reload_from_json(self, json):

"""
Replaces all attributes of the Student instance with the values from a JSON dictionary.

Args:
json (dict): A dictionary containing attribute-value pairs.
"""
for key, value in json.items():
setattr(self, key, value)
