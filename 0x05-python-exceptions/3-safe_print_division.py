#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Inside finally block: {}".format(result))

# Test cases
print(safe_print_division(10, 2))
print(safe_print_division(5, 0))
