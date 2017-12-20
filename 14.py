# Determine if 2 Strings are anagrams


def anagrams(x, y):

    if x[::-1].replace(" ", "") == y:
        return True

    return False
