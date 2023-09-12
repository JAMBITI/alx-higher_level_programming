#!/usr/bin/python3
'''Read file'''


def read_file(filename=""):
    ''' function that read file'''
    with open(filename, encoding='utf-8') as xfile:
        print(xfile.read(), end="")
