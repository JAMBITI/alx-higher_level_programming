#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        else:
            final_list.append(result)
        finally:
            final_list.append(result)
    return final_list
