#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    num = len(sys.argv) - 1
    count = 0
    for i in range(num):
        count = count + int(sys.argv[i + 1])
    print(f"{count}")
