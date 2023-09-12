#!/usr/bin/python3
"""
Module for the class Student
"""


class Student:
"""
A class representing a student
"""

def __init__(self, first_name, last_name, age):
"""
Initializes a new instance of the Student class.

Args:
first_name (str): The first name of the student.
last_name (str): The last name of the student.
age (int): The age of the student.
"""
self.first_name = first_name
self.last_name = last_name
self.age = age

def to_json(self, attrs=None):
"""
Returns a dictionary representation of the Student instance.

Args:
attrs (list): A list of attributes to include in the dictionary.

Returns:
dict: A dictionary containing the selected attributes of the Student instance.
"""
result = {}
if attrs is not None:
for attr in attrs:
if isinstance(attr, str) and hasattr(self, attr):
result[attr] = getattr(self, attr)
else:
result = self.__dict__
return result
