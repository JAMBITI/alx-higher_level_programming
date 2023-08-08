#!/usr/bin/python3
def uppercase(str):
    for l in str:
        print("{}".format(chr(ord(l) - 32) if
              (ord(l) < 123 and ord(l) >= 97) else l), end='')
    print('')
