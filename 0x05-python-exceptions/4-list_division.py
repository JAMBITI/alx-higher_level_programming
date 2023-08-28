#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, IndexError) as error:
            if isinstance(error, ZeroDivisionError):
                print("division by 0")
            elif isinstance(error, TypeError):
                print("wrong type")
            elif isinstance(error, IndexError):
                print("out of range")
            result = 0
        finally:
            final_list.append(result)
    return final_list
