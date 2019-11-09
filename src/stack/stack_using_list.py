class Stack():
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self, data):
        return self.data.append(data)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)
