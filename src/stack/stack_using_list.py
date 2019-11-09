class Stack():
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self, data):
        return self.data.append(data)

    def pop(self):
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
        if self.data:
            return len(self.data)
        else:
            return 0
