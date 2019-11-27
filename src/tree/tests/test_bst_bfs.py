from tree.bst_bfs import BinarySearchTree

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

def test_bfs():
    bst = BinarySearchTree()
    bst.insert_list([10, 15, 5, 8, 3, 20, 11, 14, 1, 4])
    assert [10, 5, 15, 3, 8, 11, 20, 1, 4, 14] == bst.bfs()