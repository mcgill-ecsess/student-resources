#Note Stacks can be implemented using LinkedLists and Arrays
class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            print(self.stack[-1])
        else:
            print("Empty")

if __name__ == "__main__":
    test_stack = Stack()
    test_stack.push(1)
    test_stack.push(2)
    test_stack.pop()
    test_stack.peek()
    test_stack.pop()
    test_stack.peek()
    test_stack.pop()