# Print all permutations of a String
from itertools import permutations


def perm(string):
    return [''.join(p) for p in permutations(string)]


def perm2(string):
    if len(string) == 1:
        return [string]

    perms = perm2(string[1:])
    char = string[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])

    return result
