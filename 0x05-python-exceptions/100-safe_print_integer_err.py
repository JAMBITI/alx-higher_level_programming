#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        error_message = "Exception: " + str(e) + "\n"
        with open("error_log.txt", "a") as f:
            f.write(error_message)
        return False
