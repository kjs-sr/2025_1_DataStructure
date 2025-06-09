import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data)

def insert(root, value):
    node = TreeNode()
    node.data = value

    if root is None:
        return node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left  # 이동
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right  # 이동
    return root

if __name__ == "__main__":
    numbers = [50, 30, 24, 5, 28, 45, 98, 52, 60]
    root = None
    for number in numbers:
        root = insert(root, number)
    post_order(root)