#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    num = len(sys.argv) - 1

    for i in range(num):
        print("{}".format(int(i) + int(sys.argv[i + 1]) ))
