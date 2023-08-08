#!/usr/bin/python3
def uppercase(str):
    for let in str:
        print("{}".format(chr(ord(let) - 32) if
              (ord(let) < 123 and ord(let) >= 97) else let), end='')
    print('')
