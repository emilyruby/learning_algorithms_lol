# Write a multiply function that multiples 2 integers without using *


def mult(x, y):  # this doesn't solve for negative integers

    if y == 0 or x == 0:
        return 0
    if y == 1:
        return x

    r = x

    for i in range(1, y):
        r += x

    return r


def mult2(x, y):  # solves negative solutions too

    if y < 0:
        return -mult2(x, -y)

    if y == 0:
        return 0

    if y == 1:
        return x

    return x + mult2(x, y - 1)
