#!/usr/bin/python3
"""Defines a class Student with a to_json method."""


class Student:
"""Represents a student with first name, last name, and age."""

def __init__(self, first_name, last_name, age):
"""Initialize a new Student.

Args:
first_name (str): The first name of the student.
last_name (str): The last name of the student.
age (int): The age of the student.
"""
self.first_name = first_name
self.last_name = last_name
self.age = age

def to_json(self):
"""Convert the Student object to a dictionary.

Returns:
dict: A dictionary representation of the Student.
"""
return {
"first_name": self.first_name,
"last_name": self.last_name,
"age": self.age
}
