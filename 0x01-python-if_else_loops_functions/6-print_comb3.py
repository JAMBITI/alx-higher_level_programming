#!/usr/bin/python3

for num in range(10, 90):
i = num // 10
j = num % 10
if j > i:
if num != 89:
print("{:02d}".format(num), end=', ')
else:
print("89")
