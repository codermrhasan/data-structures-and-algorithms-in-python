class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):

        def insert_helper(current_root, data):
            if current_root is None:
                return Node(data)

            elif data < current_root.data:
                current_root.left = insert_helper(current_root.left, data)
            
            elif data > current_root.data:
                current_root.right = insert_helper(current_root.right, data)
            
            return current_root
        
        if self.root is None:
            self.root = Node(data)
        else:
            insert_helper(self.root, data)

    def insert_list(self, new_list):
        for data in new_list:
            self.insert(data)
    
    def minimum(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node
    
    def delete(self, data):
        def delete_helper(current_root, data):
            if current_root is None:
                return current_root
            
            elif data < current_root.data:
                current_root.left = delete_helper(current_root.left, data)
            
            elif data > current_root.data:
                current_root.right = delete_helper(current_root.right, data)
            
            else:
                if current_root.left is None:
                    new_root = current_root.right
                    current_root = None
                    return new_root
                elif current_root.right is None:
                    new_root = current_root.left
                    current_root = None
                    return new_root
                else:
                    new_root = self.minimum(current_root.right)
                    current_root.data = new_root.data
                    current_root.right = delete_helper(current_root.right, new_root.data)
            
            return current_root
        delete_helper(self.root, data)