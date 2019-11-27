class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        def insert_helper(current_node, data):
            if current_node is None:
                return Node(data)
            elif data < current_node.data:
                current_node.left = insert_helper(current_node.left, data)
            elif data > current_node.data:
                current_node.right = insert_helper(current_node.right, data)
            
            return current_node
        
        if self.root is None:
            self.root = Node(data)
        else:
            insert_helper(self.root, data)
    
    def insert_list(self, data_list):
        for data in data_list:
            self.insert(data)
            
    def bfs(self, root=None):
        def bfs_helper(current_node):
            if current_node is None:
                return
            queue = []
            final_list = []
            queue.append(current_node)
            while len(queue) > 0:
                final_list.append(queue[0].data)
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return final_list
        if root is None:
            root = self.root
        
        return bfs_helper(root)
