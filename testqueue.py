# __init__(self): Initializes an empty queue.
# enqueue(self, item): Adds item to the back of the queue.
# dequeue(self): Removes and returns the front element of the queue. Returns None if the queue is empty.
# peek(self): Returns the front element of the queue without removing it. Returns None if the queue is empty.
# is_empty(self): Returns True if the queue is empty, False otherwise.
# size(self): Returns the number of elements in the queue.
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())    # prints 1
print(q.dequeue())  # prints 1
print(q.dequeue())  # prints 2
print(q.size())    # prints 1
print(q.is_empty())  # prints False
print(q.dequeue())  # prints 3
print(q.dequeue())  # prints None
print(q.is_empty())  # prints True
