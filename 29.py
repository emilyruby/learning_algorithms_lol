# Implement insertion sort


def insertion(a):
    for index in range(1, len(a)):
        current = a[index]
        position = index

        while position > 0 and a[position-1] > current:
            a[position] = a[position-1]
            position = position-1

        a[position] = current
