# Find the common elements of 2 int arrays
from sets import Set


def common(a, b):
    return list(Set(a).intersection(Set(b)))
