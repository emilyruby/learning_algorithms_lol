# Print a tree using BFS


def bfs(root):
    answer = []

    def traverse(root):
        if root.left:
            traverse(root.left)

        answer.append(root.val)

        if root.right:
            traverse(root.right)

    if root:
        traverse(root)

    return answer
