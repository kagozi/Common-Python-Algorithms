# This implementation takes a Node object root as input and recursively performs an 
# inorder traversal of the tree using the inorder_traversal() function. 
# The inorder_traversal() function takes a Node object node as input and returns a 
# list of the values of the nodes in the tree rooted at node, in ascending order. 
# The function recursively performs an inorder traversal of the left and right subtrees and 
# concatenates the results with the value of the current node in the middle.

# The is_bst() function takes the root node of the tree as input, performs the
# inorder traversal using the inorder_traversal() function, and checks if the resulting 
# sequence is sorted in ascending order. If any adjacent pair of nodes is not sorted in 
# ascending order, the function returns False. If all pairs of nodes are sorted in ascending order, 
# the function returns True.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_bst(root):
    in_order = inorder_traversal(root)
    for i in range(1, len(in_order)):
        if in_order[i] <= in_order[i-1]:
            return False
    return True


def inorder_traversal(node):
    if node is None:
        return []
    left = inorder_traversal(node.left)
    right = inorder_traversal(node.right)
    return left + [node.value] + right


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print(is_bst(root))  # prints True

root.right.right.value = 4
print(is_bst(root))  # prints False
