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
    actual = names.head.data

    assert actual == expected


def test_peek():
    """
    If we can peek data from head of linked list?
    """
    pets = SinglyLinkedList()
    pets.push('cat')
    pets.push('dog')

    expected = 'dog'
    actual = pets.peek()

    assert actual == expected


def test_get_at():
    """
    Can we get nth nodes data?
    """
    pets = SinglyLinkedList()
    pets.push('cat')
    pets.push('dog')
    pets.push('fish')
    pets.push('bird')

    expected = 'dog'
    actual = pets.get_at(2)

    assert actual == expected


def test_len():
    """
    can we get length of linked list
    """
    nums = SinglyLinkedList()
    nums.push(1)
    nums.push(2)
    nums.push(55)
    expected = 3
    actual = nums.len()

    assert actual == expected


def test_search():
    """
    can we search a value in linked list at first match and get its index
    """
    nums = SinglyLinkedList()
    nums.push(1)
    nums.push(3)
    nums.push(5)

    expected = 1
    actual = nums.search(3)
    assert actual == expected
