from linked_list.singly_linked_list import SinglyLinkedList


def test_exists():
    """
    checking existance of SinglyLinkedList class
    """
    assert SinglyLinkedList


def test_instantiation():
    """
    checking if it is successfully instantiate an empty linked list?
    """
    assert SinglyLinkedList()


def test_push():
    """
    Can we properly push a data to linked list or not? new data must be in head
    """
    names = SinglyLinkedList()
    names.push('John')
    expected = 'John'
    actual = names.head.value

    assert actual == expected
