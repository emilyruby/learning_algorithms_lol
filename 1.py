# Find the most frequent integer in an array


def frequent(array):
    f = {}
    for i in array:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    return max(f, key=f.get)


def frequent2(array):
    return max(set(array), key=array.count)
