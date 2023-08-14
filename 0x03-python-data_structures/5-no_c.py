#!/usr/bin/python3
def no_c(my_string):
    newline = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            newline += i
    return newline
