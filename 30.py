# Implement merge sort


def merge(a):

    if len(a) > 1:

        q = len(a) // 2
        l, r = a[:q], a[q:]

        merge(l)
        merge(r)

        i, j, k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            a[j] = r[j]
            j += 1
            k += 1
