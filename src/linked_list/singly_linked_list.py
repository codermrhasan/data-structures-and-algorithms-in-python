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

    def peek(self):
        return self.head.data

    def get_at(self, index):
        current = self.head
        counter = 0

        while(current and counter <= index):
            if (counter == index):
                return current.data
            counter += 1
            current = current.next_node

        raise IndexError('Invalid indexing')

    def len(self):
        current = self.head
        counter = 0

        while(current):
            counter += 1
            current = current.next_node

        return counter

    def search(self, data):
        current = self.head
        counter = 0

        while(current):
            if(current.data == data):
                return counter
            counter += 1
            current = current.next_node

        return None
