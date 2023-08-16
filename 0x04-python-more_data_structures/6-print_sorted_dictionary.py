#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    def sorted_generator(dictionary):
        for key in sorted(dictionary.keys()):
            yield key, dictionary[key]

    for i, j in sorted_generator(a_dictionary):
        print(f"{i}: {j}")
