# Check if a String is composed of all unique characters
from sets import Set


def unique(string):
    seen = Set()
    for x in string:
        if x not in seen:
            seen.add(x)
        else:
            return False
    return True


def unique2(string):
    return len(Set(string)) == len(string)
