# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in
# linear time)


def pairs(array):
    s = {}
    for i in array:
        if i in s:
            return (s[i], i)
        else:
            s[10-i] = i
