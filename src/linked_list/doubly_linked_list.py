class Node:
    """
    same as singly linked list. just we have a previous node
    """

    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next_node = self.head

        if self.head is not None:
            self.head.prev_node = new_node

        self.head = new_node

    def peek_front(self):
        return self.head.data

    def get_len(self):
        node = self.head
        counter = 0
        while node:
            counter += 1
            node = node.next_node

        return counter

    def peek_at(self, index):
        node = self.head
        counter = 0
        while node and counter <= index:
            if counter == index:
                return node.data

            counter += 1
            node = node.next_node

        raise IndexError('Invalid indexing')

    def remove_at(self, index):
        node = self.head
        counter = 0
        while node and counter <= index:
            if counter == index:
                node.prev_node.next_node = node.next_node
                node.next_node.prev_node = node.prev_node
                node = None
                return
            counter += 1
            node = node.next_node

        raise IndexError("invalid indexing")
