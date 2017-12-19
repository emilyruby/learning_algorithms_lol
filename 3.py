# Given 2 integer arrays, determine of the 2nd array is a rotated version of
# the 1st array.
# Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}


def rotate(one, two):
    print(one, two)
    if len(one) != len(two):
        return False

    for i in range(1, len(one)):
        x = one[i:] + one[:i]
        if two == x:
            return True

    return False
