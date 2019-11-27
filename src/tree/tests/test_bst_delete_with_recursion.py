from tree.bst_delete_with_recursion import BinarySearchTree

def test_instantiation():
    assert BinarySearchTree()

def test_insert():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    assert bst.root.data == 10
    assert bst.root.left.data == 5
    assert bst.root.right.data == 15

def test_insert_list():
    bst = BinarySearchTree()
    bst.insert_list([10,15,5])
    assert bst.root.data == 10
    assert bst.root.left.data == 5
    assert bst.root.right.data == 15

def test_minimum():
    bst = BinarySearchTree()
    bst.insert_list([10,15,5])
    assert bst.minimum(bst.root).data  == 5

def test_delete():
    bst = BinarySearchTree()
    bst.insert_list([10,15,5, 3, 8, 11, 20])
    bst.delete(5)
    assert bst.root.left.data == 8
    bst.delete(20)
    assert bst.root.right.right == None
    bst.delete(10)
    assert bst.root.data == 11