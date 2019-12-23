from sorting_and_searching_algorithms import binary_search

def test_binary_search():
    lst = [1,3,43,55,66]
    assert binary_search.binarySearch(lst, 43) == True
    assert binary_search.binarySearch(lst, 4545) == False