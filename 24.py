# Print the coordinates of every node in a binary tree, where root is 0,0


def coord(root):

    x = 0
    y = 0

    def traverse(root, x, y):

        if root.left:
            traverse(root.left, x - 1, y + 1)

        print((x, y))

        if root.right:
            traverse(root.right, x + 1, y + 1)

    if root:
        traverse(root, x, y)
