class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# Construct the binary tree
letters = "GLYNBERTBAQUIRAN"
nodes = [Node(letter) for letter in letters]

for i in range(len(nodes)):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(nodes):
        nodes[i].left = nodes[left]

    if right < len(nodes):
        nodes[i].right = nodes[right]

root = nodes[0]

# Display the result
print("Inorder Traversal:")
inorder(root)