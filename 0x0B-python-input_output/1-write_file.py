#!/usr/bin/python3
'''Write to a file'''


def write_file(filename="", text=""):
    '''function that Write to a file'''
    with open(filename, mode="w", encoding='utf-8') as xfile:
        return xfile.write(text)
