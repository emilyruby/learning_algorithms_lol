# Find the first non-repeated character in a String


def nrc(string):
    return min(string, key=string.count)
