# Given a lower and upper number bound, output a list of every possible
# self-dividing number, including the bounds if possible.


def selfdiv(small, large):

    answer = []

    for i in range(small, large + 1):
        if checkifselfdiv(i):
            answer.append(i)

    return answer


def checkifselfdiv(number):

    t = number

    while t:
        if not t % 10 or number % (t % 10):
            return False
        t = t // 10

    return True
