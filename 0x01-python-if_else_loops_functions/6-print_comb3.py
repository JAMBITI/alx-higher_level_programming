#!/usr/bin/python3
for x_val in range(10):
    for y_val in range(10):
        if int(x_val) >= int(y_val):
            continue
        elif int(x_val) == 8 and int(y_val) == 9:
            print("{}{}".format(x_val, y_val))
            continue
        print("{}{}, ".format(x_val, y_val), end="")
