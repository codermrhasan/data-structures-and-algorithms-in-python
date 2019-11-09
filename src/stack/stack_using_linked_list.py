class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            new_node = self.head
            self.head = self.head.next_node
            data = new_node.data
            return data
        else:
            return

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return

    def size(self):
        node = self.head
        counter = 0
        while node:
            counter += 1
            node = node.next_node
        return counter
