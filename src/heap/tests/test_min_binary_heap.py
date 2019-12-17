from heap.min_binary_heap import MinBinaryHeap

def test_exists_and_instantiation():
    assert MinBinaryHeap
    assert MinBinaryHeap()

def test_properties():
    bh = MinBinaryHeap()
    bh.heapList = [1,2,3]
    assert bh.heapList == [1,2,3]

def test_percUp():
    bh = MinBinaryHeap()
    bh.heapList = [2,3,4,1]
    bh.percUp()
    assert bh.heapList == [1,2,4,3]

def test_insert():
    bh = MinBinaryHeap()
    bh.insert(4)
    bh.insert(3)
    bh.insert(2)
    bh.insert(1)
    assert bh.heapList == [1,2,3,4]

def test_minChild():
    bh = MinBinaryHeap()
    bh.heapList = [1,2,3,4]
    assert bh.heapList[bh.minChild(0)] == 2
    assert bh.heapList[bh.minChild(1)] == 4

def test_percDown():
    bh = MinBinaryHeap()
    bh.heapList = [4,1,2,3]
    bh.percDown()
    assert bh.heapList == [1,3,2,4]

def test_delMin():
    bh = MinBinaryHeap()
    bh.heapList=[1,2,3,4]
    data = bh.delMin()
    assert data == 1
    assert bh.heapList == [2,4,3]
    bh.delMin()
    bh.delMin()
    assert bh.heapList == [4]

def test_buildHeap():
    bh = MinBinaryHeap()
    bh.buildHeap([4,3,2,1])
    assert bh.heapList == [1,3,2,4]