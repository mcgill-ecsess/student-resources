class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp

    def delete(self,val):
        current_node = self.head
        prev_node = None

        if current_node.val == val:
            self.head = self.head.next

        while current_node.next:
            if current_node.val == val:
                prev_node.next = current_node.next
                break
            prev_node = current_node
            current_node = current_node.next
            

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next
            
if __name__ == "__main__":
    linked = LinkedList()
    linked.insert(1)
    linked.insert(20)
    linked.insert(3)
    linked.delete(20)
    linked.print_all()
