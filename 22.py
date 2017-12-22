# find the 2nd largest number in a BST


def kth(root):

    answer = []

    def traverse(root):

        if root.left:
            traverse(root.left)

        answer.append(root.value)

        if root.right:
            traverse(root.right)

    if root:
        traverse(root)

    return answer[-2]


def kth2(root):

    current = root

    while root.right:
        current = root.right

    return current.value
