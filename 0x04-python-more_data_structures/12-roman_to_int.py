#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    prev_value = 0
    total = 0

    for numeral in reversed(roman_string):
        numeral_value = roman_numerals.get(numeral.upper(), 0)

        if numeral_value >= prev_value:
            total += numeral_value
        else:
            total -= numeral_value

        prev_value = numeral_value

    return total
