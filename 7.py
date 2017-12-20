# Implement binary search of a sorted array of integers
from math import floor


def binary_search(x, array):

    middle = floor(len(array) / 2)
    y = array[middle]

    if x == y:
        return y

    if not len(array):
        raise "Error"

    if x < y:
        return binary_search(x, array[:middle])
    if x > y:
        return binary_search(x, array[middle+1:])


def binary_search2(x, array):  # from stack overflow

    lower = 0
    upper = len(array)

    while lower < upper:
        y = lower + (upper - lower) // 2
        val = array[y]

        if x == val:
            return y

        elif x > val:
            if lower == y:
                break
            lower = y

        elif x < val:
            upper = y
