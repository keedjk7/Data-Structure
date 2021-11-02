class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BiTree():
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            tempRoot = self.root
            countHeight = 0
            while tempRoot != None:
                countHeight += 1
                if data < tempRoot.data:
                    if tempRoot.left == None:
                        leftNode = Node(data)
                        tempRoot.left = leftNode
                        if countHeight >self.height:
                            self.height = countHeight
                        break
                    tempRoot = tempRoot.left
                else:
                    if tempRoot.right == None:
                        rightNode = Node(data)
                        tempRoot.right = rightNode
                        if countHeight >self.height:
                            self.height = countHeight
                        break
                    tempRoot = tempRoot.right

    def printHeight(self):
        print("Height of this tree is :",self.height)


if __name__ == "__main__":
    Tree = BiTree()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        Tree.insert(i)
    Tree.printHeight()
