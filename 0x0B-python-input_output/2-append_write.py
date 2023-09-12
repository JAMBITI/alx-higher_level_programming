#!/usr/bin/python3
'''Append to a file'''


def append_write(filename="", text=""):
    '''function that Append to a file'''
    with open(filename, mode='a', encoding='utf-8') as xfile:
        return xfile.write(text)
