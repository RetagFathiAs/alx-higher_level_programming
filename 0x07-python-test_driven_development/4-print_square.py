#!/usr/bin/python3
"""
print_square module
 print a square using '#'

"""


def print_square(size):
    """Return: the n '#' of squares
    Args:
    Par: Type int
    Raises: 
    TypeError and ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
