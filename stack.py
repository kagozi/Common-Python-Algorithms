# __init__(self): Initializes an empty stack.
# push(self, item): Adds item to the top of the stack.
# pop(self): Removes and returns the top element of the stack. Returns None if the stack is empty.
# peek(self): Returns the top element of the stack without removing it. Returns None if the stack is empty.
# is_empty(self): Returns True if the stack is empty, False otherwise.
# size(self): Returns the number of elements in the stack.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())    # prints 3
print(s.pop())     # prints 3
print(s.pop())     # prints 2
print(s.size())    # prints 1
print(s.is_empty())  # prints False
print(s.pop())     # prints 1
print(s.pop())     # prints None
print(s.is_empty())  # prints True
