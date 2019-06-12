class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, val):
        if(self.head == None and self.tail == None):
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def dequeue(self):
        dequeued_node = self.head
        self.head = self.head.next
        return dequeued_node.val

    def peek(self):
        return self.head.val

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())

