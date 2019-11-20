class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    
    def add_left(self, current, data):
        new_node = Node(data)
        if current.left == None:
            current.left = new_node
        else:
            print('please correct your decision')

    def add_right(self, current, data):
        new_node = Node(data)
        if current.right == None:
            current.right = new_node
        else: 
            print('please correct your decision right')
    def preorder_print(self):
        current = self.root
        def preorder(current):
            print(current.data, end='-')
            if current.left:
                preorder(current.left)
            if current.right:
                preorder(current.right)
        preorder(current)
        print()

    def postorder_print(self):
        current = self.root
        def postorder(current):
            if current.left:
                postorder(current.left)
            if current.right:
                postorder(current.right)
            print(current.data, end='-')            
        postorder(current)
        print()


    def inorder_print(self):
        current = self.root
        def inorder(current):
            if current.left:
                inorder(current.left)
            
            print(current.data, end='-')            

            if current.right:
                inorder(current.right)
        inorder(current)
        print()



######################
##  Manual Testing  ##
######################
bt = BinaryTree(1)
bt.add_left(bt.root, 2)
bt.add_right(bt.root, 3)
bt.add_left(bt.root.left, 4)
bt.add_right(bt.root.left, 5)
bt.add_left(bt.root.right, 6)
bt.add_right(bt.root.right, 7)

# this tree looks like;
#         1
#        / \
#       /   \
#      /     \
#     2       3
#    / \     / \
#   4   5   6   7

bt.preorder_print()
# 1-2-4-5-3-6-7-
bt.postorder_print()
# 4-5-2-6-7-3-1-
bt.inorder_print()
# 4-2-5-1-6-3-7-
