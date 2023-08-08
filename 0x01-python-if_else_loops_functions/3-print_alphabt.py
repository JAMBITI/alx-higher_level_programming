#!/usr/bin/python3

for a in "abcdefghijklmnopqrstuvwxyz":
    if a == "q" or a == "e":
        continue
    print("{}".format(a), end="")
