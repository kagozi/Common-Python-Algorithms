# In this implementation, the dfs function takes a Node object as an argument and 
# prints the node's data value. It then recursively calls itself on the node's left and 
# right children, if they exist. This causes the function to explore the tree in a depth-first manner.

# To use this implementation, you would first create a binary tree by creating 
# Node objects and linking them together. Then, you would call the dfs function on 
# the root node of the tree to start the DFS traversal. For example:
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def dfs(node):
    if node is not None:
        print(node.data)
        dfs(node.left)
        dfs(node.right)


# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traverse the tree using DFS
dfs(root)
