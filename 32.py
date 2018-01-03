# Given two integers x and y, calculate the Hamming distance.


def hamming(x, y):
    return bin(x ^ y).count(1)
