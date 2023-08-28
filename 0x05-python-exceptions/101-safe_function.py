#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write(f"Exception: {e}\n")
        return None

def safe_print_integer_err(value):
    def _print(value):
        print(value)
    safe_function(_print, value)

# Test
safe_print_integer_err(42)
safe_print_integer_err("hello")
