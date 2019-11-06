class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head

        if self.head is None:
            self.head = new_node

        node = self.head

        while(node):
            if (node.next_node == None) or (node.next_node == self.head):
                self.head = new_node
                node.next_node = self.head
                return
