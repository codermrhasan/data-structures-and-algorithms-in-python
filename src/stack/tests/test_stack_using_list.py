import pytest
from stack.stack_using_list import Stack


def test_exists():
    assert Stack


def test_instanciation():
    assert Stack()


def test_isEmpty():
    mystack = Stack()
    assert mystack.isEmpty() == True


def test_push():
    mystack = Stack()
    mystack.push(1)
    mystack.push(2)
    assert mystack.data[1] == 2


@pytest.fixture
def mystack():
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    return st


def test_pop(mystack):
    m = mystack
    assert m.pop() == 5
    assert m.pop() == 4


def test_peek(mystack):
    assert mystack.peek() == 5


def test_size(mystack):
    assert mystack.size() == 5
