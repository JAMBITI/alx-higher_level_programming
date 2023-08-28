#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))

# Example usage
numerator = 10
denominator = 0

result = safe_print_division(numerator, denominator)
print("Outside result: {}".format(result))
