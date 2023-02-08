#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    for arg in sys.argv:
        if i != 0:
            print(arg)
