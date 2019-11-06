from linked_list.doubly_linked_list import DoublyLinkedList


def test_exists():
    """
    if DoublyLinkedList class exists or not
    """
    assert DoublyLinkedList


def test_instantiation():
    """
    if we can instantiate empty DoublyLinkedList
    """
    assert DoublyLinkedList()


def test_push_front():
    """
    if we can push a data to head
    """

    ls = DoublyLinkedList()
    ls.push_front(34)
    expected = 34
    actual = ls.head.data

    assert expected == actual


def test_peek_front():
    """
    if we can peek a data from front
    """
    ls = DoublyLinkedList()
    ls.push_front(1)
    ls.push_front(2)

    expected = 2
    actual = ls.peek_front()
    assert actual == expected


def test_get_len():
    """
    can we get length of list
    """
    ls = DoublyLinkedList()
    ls.push_front(44)
    ls.push_front(55)
    expected = 2
    actual = ls.get_len()
    assert expected == actual


def test_peek_at():
    """
    can we peek data from a certain index
    """
    ls = DoublyLinkedList()
    ls.push_front(44)
    ls.push_front(55)
    ls.push_front(66)
    expected = 55
    actual = ls.peek_at(1)
    assert actual == expected


def test_remove_at():
    """
    can we remove at a certain point by index number
    the ease of doubly linked list is here
    """
    ls = DoublyLinkedList()
    ls.push_front(1)
    ls.push_front(2)
    ls.push_front(55)
    ls.push_front(6)

    ls.remove_at(1)
    expected = 2
    actual = ls.peek_at(1)
    assert actual == expected
