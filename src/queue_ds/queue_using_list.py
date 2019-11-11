class Queue:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def enqueue(self, data):
        self.data.insert(0, data)

    def dequeue(self):
        if self.data:
            return self.data.pop()
        else:
            return

    def peek(self):
        if self.data:
            return self.data[len(self.data)-1]
        else:
            return

    def size(self):
        return len(self.data)
