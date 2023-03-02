# A binary tree is balanced if the difference between the heights of its left and 
# right subtrees is at most 1 for every node in the tree.
# This implementation takes a Node object root as input and recursively 
# checks if the tree is balanced. The is_balanced() function first checks if 
# the root node is None and returns True if it is . Otherwise, it calculates the heights of 
# the left and right subtrees using the get_height() function. If the absolute difference 
# between the heights is greater than 1, the tree is unbalanced and the function returns False. 
# If the tree is balanced at the current node, the function recursively checks if the left and 
# right subtrees are balanced.

# The get_height() function takes a Node object node as input and 
# recursively calculates the height of the tree rooted at node. If node is None, 
# the function returns 0. Otherwise, it recursively calculates the heights of the left and 
# right subtrees and returns the maximum height plus 1.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_balanced(root):
    if root is None:
        return True

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)


def get_height(node):
    if node is None:
        return 0

    return max(get_height(node.left), get_height(node.right)) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(is_balanced(root))  # prints True

root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)
print(is_balanced(root))  # prints False
