# Given two binary trees and imagine that when you put one of them to cover
# the other, some nodes of the two trees are overlapped while the others are
# not.
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def merge(a, b):

    if not a and not a:
        return None

    answer = TreeNode(0)

    def traverse(a, b):
        if a and b:
            answer.val = a.val + b.val
        if a and not b:
            answer.val = a.val
        if not a and b:
            answer.val = b.val

        if a.left or b.left:
            traverse(a.left, b.left, answer.left)

        if a.right or b.right:
            traverse(a.right, b.right, answer.right)

    if a or b:
        traverse(a, b, answer)

    return answer


def merge2(a, b):

    if not a and not b:
        return None

    answer = TreeNode((a.val if a else 0) + (b.val if b else 0))
    answer.left = merge2(a and a.left, b and b.left)
    answer.right = merge2(a and a.right, b and b.right)

    return answer
