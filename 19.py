# Print a tree using DFS


def dfs(root):
    answer = []

    def traverse(root):
        answer.append(root.val)

        if root.left:
            traverse(root.left)

        if root.right:
            traverse(root.right)

    if root:
        traverse(root)

    return answer
