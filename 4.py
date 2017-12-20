# Find the only element in an array that only occurs once.
from sets import Set


def once(array):
    seen = Set()
    seen2 = Set()
    for i in array:
        if i not in seen2:
            if i in seen:
                seen2.add(i)
                seen.remove(i)
            else:
                seen.add(i)
    return list(seen)
