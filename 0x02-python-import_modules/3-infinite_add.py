#!/usr/bin/python3
    import sys
if __name__ == "__main__":

    a = 0
    args = sys.argv

    if len(args) > 1:
        for arg in sys.argv[1:]:
        a += int(arg)

    print(a)
