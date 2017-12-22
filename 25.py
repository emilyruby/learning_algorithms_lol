# Print a tree by levels


def levels(root):

    if not root:
        return []

    level = [root]
    answer = [[root.val]]

    while level:

        next_level = []
        values = []

        for node in level:

            if node.left:
                next_level.append(node.left)
                values.append(node.left.value)

            if node.right:
                next_level.append(node.right)
                values.append(node.right.value)

        level = next_level

        if values:
            answer.append(values)

    return answer












