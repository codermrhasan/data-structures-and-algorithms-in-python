import pytest
from queue_ds.queue_using_list import Queue


def test_exists():
    assert Queue


def test_instantiation():
    assert Queue()


def test_isEmpty():
    assert Queue().isEmpty() == True


def test_enqueue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.data[0] == 2


@pytest.fixture
def filled_q():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    return q


@pytest.fixture
def empty_q():
    return Queue()


def test_dequeue(filled_q, empty_q):
    q = filled_q
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert empty_q.dequeue() == None


def test_peek(filled_q, empty_q):
    q = filled_q
    assert q.peek() == 1
    assert empty_q.peek() == None


def test_size(filled_q, empty_q):
    q = filled_q
    assert q.size() == 5
    q.dequeue()
    assert q.size() == 4
    assert empty_q.size() == 0
