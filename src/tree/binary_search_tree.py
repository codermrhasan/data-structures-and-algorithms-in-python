class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    
    ################################
    ######### BST Insert ###########
    ################################
    
    def insert(self, data):
        
        def insert_helper(current_node, new_node):
            if current_node.data == new_node.data:
                print(f'---> {new_node.data} <--- is a duplicate key. This data insertion will be skipped.')
                return
            elif current_node.data < new_node.data:
                if current_node.right is None:
                    new_node.parent = current_node
                    current_node.right = new_node
                else:
                    insert_helper(current_node.right, new_node)
            else:
                if current_node.left is None:
                    new_node.parent = current_node
                    current_node.left = new_node
                else:
                    insert_helper(current_node.left, new_node)
        
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
        else:    
            insert_helper(self.root, new_node)
    

    def insert_list(self, new_list):
        for data in new_list:
            self.insert(data)
    
    #################################
    ######### All Traversal #########
    #################################
    
    def get_inorder_list(self, node, lst):
        if node:
            if node.left:
                self.get_inorder_list(node.left, lst)
            if node.data:
                lst.append(node.data)
            if node.right:
                self.get_inorder_list(node.right, lst)

            # if want to return something, return when left and right both node is none    
            if node.left is None and node.right is None:
                return lst  
        return lst
    
    def get_preorder_list(self, node, lst):
        if node:
            if node.data:
                lst.append(node.data)
            if node.left:
                self.get_preorder_list(node.left, lst)
            if node.right:
                self.get_preorder_list(node.right, lst)

            # if want to return something, return when left and right both node is none    
            if node.left is None and node.right is None:
                return lst  
        return lst
    
    def get_postorder_list(self, node, lst):
        if node:
            if node.left:
                self.get_postorder_list(node.left, lst)
            if node.right:
                self.get_postorder_list(node.right, lst)
            if node.data:
                lst.append(node.data)
                
            # if want to return something, return when left and right both node is none    
            if node.left is None and node.right is None:
                return lst  
        return lst
    
    ################################
    ########## All Print ###########
    ################################
    
    def print_inorder(self):
        lst = self.get_inorder_list(self.root, [])
        print(lst)
        return lst
    
    def print_preorder(self):
        lst = self.get_preorder_list(self.root, [])
        print(lst)
        return lst
    
    def print_postorder(self):
        lst = self.get_postorder_list(self.root, [])
        print(lst)
        return lst
    
    ################################
    ############ Search ############
    ################################
    
    def search(self, find_data):
        def search_helper(current_node, find_data):
            if current_node is None:
                print('Not Found')
                return current_node
            if current_node.data == find_data:
                return current_node
            elif current_node.data > find_data:
                return search_helper(current_node.left, find_data)
            else:
                return search_helper(current_node.right, find_data)
        
        return search_helper(self.root, find_data)
    
    ################################
    ##### Minimum and Maximum ######
    ################################
    
    def minimum(self, current_node=None):
        if current_node==None:
            current_node=self.root
            
        while current_node.left:
            current_node = current_node.left
            
        return current_node
    
    def maximum(self, current_node=None):
        if current_node==None:
            current_node=self.root
            
        while current_node.right:
            current_node = current_node.right
            
        return current_node
            
    
    
    ################################
    ########### Deleting ###########
    ################################
    
    def delete(self, data):
        node_to_delete = self.search(data)
        
        # if node_to_delete is leaf node, simply remove this leaf node
        if (node_to_delete.left is None) and (node_to_delete.right is None):
            
            # if node_to_delete is root
            if node_to_delete.parent == None:
                self.root = None
            
            # if node_to_delete is the left child of its parent
            elif node_to_delete.parent.left == node_to_delete:
                node_to_delete.parent.left = None
                
            # if node_to_delete is the right child
            else:
                node_to_delete.parent.right = None

        # if node_to_delete has only right child, change with right child
        elif node_to_delete.left is None:
            node_to_delete.right.parent = node_to_delete.parent
            
            # if node_to_delete is root
            if node_to_delete.parent == None:
                self.root = node_to_delete.right
                
            # if node_to_delete is left child
            elif node_to_delete.parent.left == node_to_delete:
                node_to_delete.parent.left = node_to_delete.right
                
            # if node_to_delete is right child
            else:
                node_to_delete.parent.right = node_to_delete.right

        # if node_to_delete has only left child change with left child
        elif node_to_delete.right is None:
            node_to_delete.left.parent = node_to_delete.parent
            
            # if node_to_delete is root
            if node_to_delete.parent == None:
                self.root = node_to_delete.left

            # if node_to_delete is left child
            elif node_to_delete.parent.left == node_to_delete:
                node_to_delete.parent.left = node_to_delete.left
            
            # if node_to_delete is right child
            else:
                node_to_delete.parent.right = node_to_delete.left
        
        
        # if node_to_delete has both child
        # change with successor(next greater node of node_to_delete on the tree)
        # that means change with smallest node of right subtree of node_to_delete
        else:
            # get the successor
            next_smaller = self.minimum(node_to_delete.right)
            
            # if next_smaller is the direct child of node_to_delete
            if next_smaller.parent == node_to_delete:
                next_smaller.parent = node_to_delete.parent
                node_to_delete.left.parent = next_smaller
                next_smaller.left = node_to_delete.left
                
                
                # if node_to_delete is root node
                if node_to_delete.parent is None:
                    self.root = next_smaller
                
                # if node_to_delete is left child
                elif node_to_delete.parent.left == node_to_delete:                    
                    node_to_delete.parent.left = next_smaller
                
                # if node_to_delete is right child
                else:
                    node_to_delete.parent.right = next_smaller
                
            # if next_smaller is not the direct child of node_to_delete
            else:
                # if next_smaller has right child
                if next_smaller.right:
                    next_smaller.right.parent = next_smaller.parent
                    next_smaller.parent.left = next_smaller.right
                
                # if next_smaller is leaf node
                else:
                    next_smaller.parent.left = None
                
                next_smaller.parent = node_to_delete.parent
                node_to_delete.right.parent = next_smaller
                node_to_delete.left.parent = next_smaller
                next_smaller.right = node_to_delete.right
                next_smaller.left = node_to_delete.left
                
                # if node_to_delete is the root node
                if node_to_delete.parent is None:
                    self.root = next_smaller
                
                # if node_to_delete is the left child
                elif node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = next_smaller
                
                # if node_to_delte is the right child
                else:
                    node_to_delete.parent.right = next_smaller
            
