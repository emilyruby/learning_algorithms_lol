# Write a function that determines if a tree is a BST


def bst(root):

    answer = []

    def traverse(root):
        if root.left:
            traverse(root.left)
        answer.append(root.value)
        if root.right:
            traverse(root.right)

    if root:
        traverse(root)

    if answer:
        l = answer[0]
        for i in range(1, len(answer)):
            if l < answer[i]:
                pass
            else:
                return False
            l = answer[i]
    else:
        return True

    return True
