class node:
    def __init__(self,van,day) :
        self.van = van
        self.day = day

    def __str__(self):
        return str(self.van)

class MinHeap:
    def __init__(self,capacity):
        self.storage = [0] * capacity
        self.van = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self,index):
        return (index-1) // 2
    def getLeftChildIndex(self,index):
        return 2* index + 1
    def getRightChildIndex(self,index):
        return 2 * index + 2

    def hasParent(self,index):
        return self.getParentIndex(index) >= 0
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size

    def parent(self,index):
        return self.storage[self.getParentIndex(index)]
    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity
    def swap(self,index1,index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self,data):
        if self.isFull():
            while self.storage[0] != 0:
                self.use_van()
            if self.storage[0] == 0:
                self.removeMin()
        self.storage[self.size] = data
        sendBack = None
        for i in range (len(self.van)):
            if self.van[i] == 0:
                self.van[i] = data
                sendBack = i+1
                break
        self.size += 1 
        self.heapifyUp(self.size - 1)

        return sendBack

    def heapifyUp(self,index):
        if self.hasParent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getParentIndex(index),index)
            self.heapifyUp(self.getParentIndex(index))

    def removeMin(self):
        if self.size == 0:
            print('Empty Heap')
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)

    def heapifyDown(self,index):
        smallestChildIndex = index
        if self.hasLeftChild(index) and self.storage[smallestChildIndex] > self.leftChild(index):
            smallestChildIndex = self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.storage[smallestChildIndex] > self.rightChild(index):
            smallestChildIndex = self.getRightChildIndex(index)
        if smallestChildIndex != index:
            self.swap(index,smallestChildIndex)
            self.heapifyDown(smallestChildIndex)

    def use_van(self):
        for i in range(len(self.storage)):
            if self.storage[i] > 0 :
                self.storage[i] -= 1
                self.van[i] -= 1


if __name__ == '__main__':
    k,order = input('Enter Input : ').split('/')

    heap = MinHeap(int(k))

    list_order = []
    
    for i in order.split(' '):
        list_order.append(int(i))

    for i in range (len(list_order)):
        van = heap.insert(list_order[i])
        print('Customer {} Booking Van {} | {} day(s)'.format(i+1,van,list_order[i]))

    



    