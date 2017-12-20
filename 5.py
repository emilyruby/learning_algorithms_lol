# Write fibbonaci iteratively and recursively (bonus: use dynamic programming)


def fib_recursive(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib_recursive(x - 1) + fib_recursive(x - 2)


def fib_iterative(x):
    if x < 2:
        return x
    else:
        result = [1, 1]
        for i in range(2, x):
            result.append(result[i - 2] + result[i - 1])
        return result[x - 1]
