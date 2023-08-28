#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for index, item in enumerate(my_list):
        if index < x:
            try:
                print(item, end='')
                count += 1
            except IndexError:
                break
        else:
            break
    print()
    return count
