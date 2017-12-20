# Reverse a String iteratively and recursively


def rev1(string):
    r = ''
    for i in range(len(string)-1, -1, -1):
        r += string[i]
    return r


def rev2(string):
    if len(string) == 1:
        return string

    return string[-1] + rev2(string[:-1])
