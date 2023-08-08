#!/usr/bin/python3

for a in range(10):
    for b in range(10):
        if b > i:
            if a * 10 + b != 89:
                print("{:02d}".format(a * 10 + b), end=', ')
            else:
                print("89")
