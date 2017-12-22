# Given a binary tree which is a sum tree (child nodes add to parent),
# write an algorithm to determine whether the tree is a valid sum tree


def sum_tree(root):

    a = 0
    b = 0

    while root:

        a, b = 0

        if root.left:
            a = root.left.value

        if root.right:
            b = root.right.value

        if (a + b) != root.value:
            return False

    return True
