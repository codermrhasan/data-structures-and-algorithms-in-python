from heap.min_binary_heap import MinBinaryHeap

def test_exists_and_instantiation():
    assert MinBinaryHeap
    assert MinBinaryHeap()

def test_properties():
    bh = MinBinaryHeap()
    bh.heapList = [1,2,3]
    assert bh.heapList == [1,2,3]
    assert len(bh.heapList) == 3

def test_percUp():
    bh = MinBinaryHeap()
    bh.heapList = [6, 8, 3, 1]
    bh.percUp()
    assert bh.heapList == [1, 6, 3, 8]

def test_insert():
    bh = MinBinaryHeap()
    bh.insert(6)
    bh.insert(8)
    bh.insert(3)
    bh.insert(1)
    assert bh.heapList == [1, 3, 8, 6]

def test_minChild():
    bh = MinBinaryHeap()
    bh.heapList = [1,3,8,6]
    assert bh.heapList[bh.minChild(0)] == 3
    assert bh.heapList[bh.minChild(1)] == 6

def test_percDown():
    bh = MinBinaryHeap()
    bh.heapList = [8,1,4,6]
    bh.percDown()
    assert bh.heapList == [1,6,4,8]

def test_delMin():
    bh = MinBinaryHeap()
    bh.insert(8)
    bh.insert(6)
    bh.insert(11)
    bh.insert(1)
    assert bh.heapList == [1,6,11,8]
    removedata = bh.delMin()
    assert removedata == 1
    assert bh.heapList == [6,8,11]

def test_buildHeap():
    bh = MinBinaryHeap()
    bh.buildHeap([4,21,11,12])
    assert bh.heapList == [4,12,11,21]