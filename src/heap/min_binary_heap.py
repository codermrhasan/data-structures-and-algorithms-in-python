class MinBinaryHeap:
    def __init__(self):
        self.heapList = []

    def percUp(self):
        heapSize = len(self.heapList)
        print(heapSize)
        index = heapSize-1
        
        while(index//2 >= 0):
            if self.heapList[index] < self.heapList[index//2]:
                temp = self.heapList[index]
                self.heapList[index] = self.heapList[index//2]
                self.heapList[index//2] = temp
            index = index//2
            if index == 0: 
                break
    
    def insert(self, data):
        self.heapList.append(data)
        self.percUp()

    def minChild(self, index):
        rightChildIndex = index*2+2
        lastIndex = len(self.heapList)-1
        leftChildIndex = index*2+1

        if leftChildIndex==lastIndex:
            return leftChildIndex
        
        if self.heapList[leftChildIndex] < self.heapList[rightChildIndex]:
            return leftChildIndex
        
        return rightChildIndex

    def percDown(self, index=0):
        lastIndex = len(self.heapList)-1
        leftChildIndex = index*2+1

        while(leftChildIndex <= lastIndex):
            minChildIndex = self.minChild(index)
            if self.heapList[index]>self.heapList[minChildIndex]:
                temp = self.heapList[index]
                self.heapList[index] = self.heapList[minChildIndex]
                self.heapList[minChildIndex] = temp
            index = minChildIndex
            leftChildIndex = index*2+1
        
    def delMin(self):
        data = self.heapList[0]
        lastIndex = len(self.heapList)-1
        self.heapList[0] = self.heapList[lastIndex]
        self.heapList.pop()
        self.percDown()
        return data

    def buildHeap(self, alist):
        lastIndex = len(alist)-1
        parentIndex = lastIndex//2
        self.heapList = alist
        while( parentIndex >= 0 ):
            self.percDown(parentIndex)
            parentIndex -= 1
