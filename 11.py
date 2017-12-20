# given a function rand5() that returns a random int between 0 and 5,
# implement rand7()


def rand2():
    x = rand5()

    if x == 4:
        return rand2()

    else:
        return x % 2


def rand7():
    x = rand2() * 4 + rand2() * 2 + rand2()

    if x == 7:
        return rand7()

    else:
        return x
