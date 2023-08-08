#!/usr/bin/python3
def convert_to_uppercase(input_str):
    for letter in input_str:
        print("{}".format(chr(ord(letter) - 32) if
              (ord(letter) < 123 and ord(letter) >= 97) else letter), end='')
    print('')
