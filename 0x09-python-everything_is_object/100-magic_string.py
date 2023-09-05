#!/usr/bin/python3


def magic_string(counter=[0]):
    counter[0] += 1
    return "BestSchool" + (", BestSchool" * (counter[0] - 1))

# Example usage
for _ in range(5):
    print(magic_string())
