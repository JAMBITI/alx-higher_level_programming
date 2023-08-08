#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
    num = -num
line = "Last digit of {} is {} and is {}"
if num > 5:
    print(line.format(number, num, "greater than 5"))
elif num < 6 and num != 0:
    print(line.format(number, num, "less than 6 and not 0"))
else:
    print(line.format(number, num, "0"))
