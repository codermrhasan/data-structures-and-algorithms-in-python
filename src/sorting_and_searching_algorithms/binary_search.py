# Binary Search algorithm

def binarySearch(alist, item):
    """
    to use this function you must have a sorted array/list.
    """
    firstIndex = 0
    lastIndex = len(alist)-1
    found = False
    
    while firstIndex<=lastIndex:
        midIndex = (firstIndex+lastIndex)//2
        if alist[midIndex] == item:
            found = True
            break
        else:
            if item < alist[midIndex]:
                lastIndex = midIndex - 1
            else:
                firstIndex = midIndex + 1
    return found
