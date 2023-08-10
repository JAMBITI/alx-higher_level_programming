#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenth = len(sys.argv[1:])
    if lenth == 0:
        print("0 arguments.")
    elif lenth == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(lenth))
    for x in range(lenth):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
