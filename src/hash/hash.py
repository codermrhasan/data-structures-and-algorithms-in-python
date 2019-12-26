from linked_list.singly_linked_list import SinglyLinkedList

class HashTable():
    def __init__(self, size, hash_type='sum'):
        if hash_type != 'sum' and != 'mult':
            raise ValueError("must have 'sum' or 'mult' value")
        self.hash_list = []
        self.size = size
        self.hash_type = hash_type

        for i in range(size):
            self.hash_list.append(SinglyLinkedList())

    def sum_hash(self, string):
        total = 0
        for letter in string:
            total += ord(letter)
        return total

    def mult_hash(self, string):
        total = 1
        for letter in string:
            total *= ord(letter)
        return total
    
    def put(self, key, value):
        if type(key) is not str:
            raise TypeError('key must be str')

        if self.hash_type == 'sum':
            key_hash = self.sum_hash(key)

        if self.hash_type == 'mult':
            key_hash = self.mult_hash(key)

        index = key_hash % self.size
        self.hash_list[index].push([key, value])

    def get(self, key):
        if type(key) is not str:
            raise TypeError('key must be str')
        if self.hash_type == 'sum':
            key_hash = self.sum_hash(key)
        if self.hash_type == 'mult':
            key_hash = self.mult_hash(key)

        index = key_hash % self.size
        
        currentNode = self.hash_list[index].head
        
        while currentNode is not None:
            if currentNode.val[0] == key:
                return currentNode.val[1]
            currentNode = currentNode.next_node
        
        return None

    def update(self, key, value):
        if type(key) is not str:
            raise TypeError('key must be str')
        if self.hash_type == 'sum':
            key_hash = self.sum_hash(key)
        if self.hash_type == 'mult':
            key_hash = self.mult_hash(key)

        index = key_hash % self.size
        currentNode = self.hash_list[index].head

        while currentNode is not None:
            if currentNode.val[0] == key:
                currentNode.val[1] = value
                return self.hash_list[index]
            currentNode = currentNode.next_node

        raise ValueError('Key not found')
    
    def remove(self, key):
        if type(key) is not str:
            raise TypeError('key must be str')
        if self.hash_type == 'sum':
            key_hash = self.sum_hash(key)
        if self.hash_type == 'mult':
            key_hash = self.mult_hash(key)
        
        index = key_hash % self.size
        
        value = [key, slef.get(key)]
        self.hash_list[index].remove(value)
        return self.hash_list[index]

    def keys(self):
        output_list = set()
        for bucket in self.hash_list:
            if len(bucket)>0:
                current = bucket.head

                while current is not None:
                    output_list.add(current.val[0])
                    current = current.next_node

        return output_list
        