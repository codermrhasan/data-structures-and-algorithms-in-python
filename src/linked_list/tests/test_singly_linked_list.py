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


def test_insert_at():
    """
    can we insert at a given index?
    """
    nums = SinglyLinkedList()
    nums.push(1)
    nums.push(3)
    nums.push(54)

    expected = 3
    actual = nums.get_at(1)
    assert actual == expected

    nums.insert_at(1, 666)
    expected = 666
    actual = nums.get_at(1)
    assert actual == expected


def test_append():
    """
    can we insert data at the end?
    """
    nums = SinglyLinkedList()
    nums.push(1)
    nums.push(3)

    nums.append(55)
    expected = 55
    actual = nums.get_at(2)
    assert actual == expected


def test_pop():
    """
    can we remove data from head? pop will return the removed data
    """
    nums = SinglyLinkedList()
    nums.push(1)
    nums.push(2)

    expected = 2
    actual = nums.pop()
    assert expected == actual

    expected = 1
    actual = nums.peek()
    assert expected == actual
