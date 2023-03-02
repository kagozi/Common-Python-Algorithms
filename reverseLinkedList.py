# Initialize a prev pointer to None, a curr pointer to head, and a next_node pointer 
# to the next node after curr.
# Iterate through the linked list. For each node:
# Set next_node to the next node after curr.
# Set curr.next to prev to reverse the link between curr and prev.
# Update prev to curr.
# Update curr to next_node.
# Return the new prev, which is the new head of the reversed linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# reverse the linked list
new_head = reverse_list(head)

# print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
while new_head:
    print(new_head.value, end=" -> ")
    new_head = new_head.next
