#!/usr/bin/python3


def magic_string():
    i = 0
    while True:
        i += 1
        yield "BestSchool" + (", BestSchool" * (i - 1))

# Example usage:
gen = magic_string()
for _ in range(5):  # Generate 5 strings
    print(next(gen))
