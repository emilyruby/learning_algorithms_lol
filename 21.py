# Find the smallest element in a BST


def smallest(root):  # a bit more flexible because you could find kth smallest

    answer = []

    def in_order(root):
        if root.left:
            in_order(root.left)
        answer.append(root.val)
        if root.right:
            in_order(root.right)

    if root:
        in_order(root)

    return answer[0]


def smallest2(root):  # more efficient for finding smallest

    current = root

    while current.left:
        current = current.left

    return current.value
