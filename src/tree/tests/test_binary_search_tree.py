from tree.binary_search_tree import BinarySearchTree 
import pytest

def test_exists():
    assert BinarySearchTree

def test_instantiation():
    assert BinarySearchTree()

def test_insert():
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(10)
    bst.insert(1)
    assert bst.root.data == 4
    assert bst.root.left.data == 1
    assert bst.root.right.data == 10

def test_insert_list():
    bst = BinarySearchTree()
    bst.insert_list([10,5,17])
    assert bst.root.data == 10
    assert bst.root.left.data == 5
    assert bst.root.right.data == 17

@pytest.fixture
def bst():
    b = BinarySearchTree()
    b.insert_list([10,5,17,3,7,12,19,1,4,13])
    return b

def test_get_inorder_list(bst):
    actual = bst.get_inorder_list(bst.root, [])
    expected = [1, 3, 4, 5, 7, 10, 12, 13, 17, 19]
    assert actual == expected

def test_get_preorder_list(bst):
    actual = bst.get_preorder_list(bst.root, [])
    expected = [10, 5, 3, 1, 4, 7, 17, 12, 13, 19]
    assert actual == expected

def test_get_postorder_list(bst):
    actual = bst.get_postorder_list(bst.root, [])
    expected = [1, 4, 3, 7, 5, 13, 12, 19, 17, 10]
    assert actual == expected

def test_print_inorder(bst):
    actual = bst.print_inorder()
    expected = [1, 3, 4, 5, 7, 10, 12, 13, 17, 19]
    assert actual == expected

def test_print_preorder(bst):
    actual = bst.print_preorder()
    expected = [10, 5, 3, 1, 4, 7, 17, 12, 13, 19]
    assert actual == expected

def test_print_postorder(bst):
    actual = bst.print_postorder()
    expected = [1, 4, 3, 7, 5, 13, 12, 19, 17, 10]
    assert actual == expected

def test_search(bst):
    assert bst.search(4).data == 4
    assert bst.search(12).data == 12
    assert bst.search(-1) == None

def test_minimum(bst):
    assert bst.minimum().data == 1
    assert bst.minimum(bst.search(17)).data == 12

def test_maximum(bst):
    assert bst.maximum().data == 19
    assert bst.maximum(bst.search(5)).data == 7

def test_delete(bst):
    bt = bst
    bt.delete(10)
    assert bt.print_inorder() == [1, 3, 4, 5, 7, 12, 13, 17, 19]
    bt.delete(4)
    assert bt.print_inorder() == [1, 3, 5, 7, 12, 13, 17, 19]
    bt.delete(17)
    assert bt.print_inorder() == [1, 3, 5, 7, 12, 13, 19]
    bt.delete(12)
    assert bt.print_inorder() == [1, 3, 5, 7, 13, 19]
    bt.delete(1)
    bt.delete(5)
    bt.delete(3)
    assert bt.print_inorder() ==   [7, 13, 19]
    bst.delete(19)
    bst.delete(13)
    assert bt.print_inorder() == [7]
    bst.delete(7)
    assert bt.print_inorder() == []

