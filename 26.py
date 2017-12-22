# Implement bubble sort


def bubble(a):
    length = len(a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if a[i] > a[i+1]:
                sorted = False
                a[i], a[i+1] = a[i+1], a[i]


def bubble2(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
