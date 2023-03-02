# In this implementation, the bfs function takes a Node object as an argument and 
# prints the node's data value. It uses a queue list to keep track of nodes to visit, 
# starting with the initial node. It then enters a loop where it pops the first node 
# from the queue and visits it, printing its data value. It then adds its left and 
# right children to the end of the queue, if they exist. This causes the function to 
# explore the tree in a breadth-first manner.

# To use this implementation, you would first create a binary tree by creating Node 
# objects and linking them together. Then, you would call the bfs function on the root 
# node of the tree to start the BFS traversal.


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def bfs(node):
    queue = []
    queue.append(node)
    while queue:
        curr = queue.pop(0)
        print(curr.data)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traverse the tree using BFS
bfs(root)
