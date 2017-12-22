# Implement selection sort


def selection(a):

    for i in range(len(a) - 1, 0, -1):

        maxi = 0

        for location in range(1, i + 1):

            if a[location] > a[maxi]:
                maxi = location

        a[i], a[maxi] = a[maxi], a[i]
