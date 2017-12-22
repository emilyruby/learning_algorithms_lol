# Given 2 trees, verify the second tree is a subtree of the other


def subtree(root, root2):

    if not root2:
        return True

    if not root and root2:
        return False

    tree1 = []
    tree2 = []

    def traverse(root, values):

        if root.left:
            traverse(root.left)

        values.append(root.value)

        if root.right:
            traverse(root.right)

    if root:
        traverse(root, tree1)

    if root2:
        traverse(root, tree2)

    return tree1 == tree2


def subtree2(one, two):

    def match(one, two):

        if not (one and two):
            return False

        if one.value == two.value:
            return subtree2(one.left, two.left) and subtree2(one.right, two.right)

    if match(one, two):
        return True

    if not one:
        return False

    return subtree2(one.left, two) or subtree2(one.right, two)
