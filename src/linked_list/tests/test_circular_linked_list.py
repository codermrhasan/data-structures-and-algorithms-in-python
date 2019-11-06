from linked_list.circular_linked_list import CircularLinkedList


def test_exists():
    """
    if CircularLinkedList class exists or not
    """
    assert CircularLinkedList


def test_instantiation():
    """
    if we can instantiate empty CircularLinkedList
    """
    assert CircularLinkedList()


def test_push():
    """
    if we can push a data to head using circular linked list
    """

    ls = CircularLinkedList()
    ls.push(34)
    ls.push(3)
    expected = 3
    actual = ls.head.next_node.next_node.data

    assert expected == actual
