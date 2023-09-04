#!/usr/bin/python3
"""
Module to separate text based on delimiters
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: Input text as a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = [".", "?", ":"]
    new_lines = []
    current_line = ""

    for letter in text:
        current_line += letter
        if letter in delimiters:
            new_lines.append(current_line.replace(" \n", "\n").replace("\n ", "\n"))
            current_line = ""

    if current_line:
        new_lines.append(current_line.replace(" \n", "\n").replace("\n ", "\n"))

    for line in new_lines:
        print(line.strip(" \t"), end="")
        for delimiter in delimiters:
            if delimiter in line:
                print(end="\n\n")
                break
