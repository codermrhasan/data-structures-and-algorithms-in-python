from heap.max_binary_heap import MaxBinaryHeap

def test_exists_and_instantiation():
    assert MaxBinaryHeap
    assert MaxBinaryHeap()

def test_properties():
    bh = MaxBinaryHeap()
    bh.heapList = [1,2,3]
    assert bh.heapList == [1,2,3]

def test_percUp():
    bh = MaxBinaryHeap()
    bh.heapList = [3,2,1,4]
    bh.percUp()
    assert bh.heapList == [4,3,1,2]

def test_insert():
    bh = MaxBinaryHeap()
    bh.insert(1)
    bh.insert(2)
    bh.insert(3)
    bh.insert(4)
    assert bh.heapList == [4,3,2,1]

def test_maxChild():
    bh = MaxBinaryHeap()
    bh.heapList = [4,3,2,1]
    assert bh.heapList[bh.maxChild(0)] == 3
    assert bh.heapList[bh.maxChild(1)] == 1

def test_percDown():
    bh = MaxBinaryHeap()
    bh.heapList = [1,4,3,2]
    bh.percDown()
    assert bh.heapList == [4,2,3,1]

def test_delMax():
    bh = MaxBinaryHeap()
    bh.heapList=[4,3,2,1]
    data = bh.delMax()
    assert data == 4
    assert bh.heapList == [3,1,2]
    bh.delMax()
    bh.delMax()
    assert bh.heapList == [1]

def test_buildHeap():
    bh = MaxBinaryHeap()
    bh.buildHeap([1,2,3,4])
    assert bh.heapList == [4,2,3,1]