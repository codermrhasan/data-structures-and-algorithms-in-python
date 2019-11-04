class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
