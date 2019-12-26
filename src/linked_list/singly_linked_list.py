class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        self.itr = self.head
        return self

    def __next__(self):
        if self.itr:
            data = self.itr.data
            self.itr = self.itr.next_node
            return data
        else:
            raise StopIteration

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

        return

    def insert_at(self, index, data):
        prev_node = self.head
        counter = 0
        if not index:
            print("for this type of operation we have push()")
            return

        while(prev_node):
            if(counter == index-1):
                new_node = Node(data)
                new_node.next = prev_node.next_node
                prev_node.next_node = new_node

            counter += 1
            prev_node = prev_node.next_node

    def append(self, data):
        current = self.head
        while(current):
            if not current.next_node:
                new_node = Node(data)
                current.next_node = new_node
                return
            current = current.next_node

    def pop(self):
        data = self.head.data
        self.head = self.head.next_node
        return data

    def remove_at(self, index):
        prev_node = self.head
        counter = 0
        data = 0

        if not index:
            print("for this type of operation we have pop()")
            return

        while(prev_node):
            if(counter == index-1):
                data = prev_node.next_node.data
                prev_node.next_node = prev_node.next_node.next_node
                return data
            counter += 1
            prev_node = prev_node.next_node
    
    def remove(self, data):
        prev_node = self.head
        data = 0

        while(prev_node):
            if(data == prev_node.next_node.data):
                data = prev_node.next_node.data
                prev_node.next_node = prev_node.next_node.next_node
                return data
            prev_node = prev_node.next_node