# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.


def rev(a):
    answer = []
    words = a.split(' ')
    for word in words:
        answer.append(word[::-1])
    return ' '.join(answer)
