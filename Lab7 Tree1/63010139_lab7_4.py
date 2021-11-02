

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue():
    def __init__ (self):
        self.list = []

    def enQueue (self,i):
        self.list.append(i)

    def deQueue(self):
        return self.list.pop(0)

    def isEmpty(self):
        return len(self.list) == 0

    def printAll(self):
        while self.isEmpty() != True:
            DQ = self.deQueue()
            print(str(DQ) + ' ',end='')

class BiTree():
    def __init__(self):
        self.root = None
        self.queue = Queue()

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            tempRoot = self.root
            while tempRoot!=None:
                if data<tempRoot.data:
                    if tempRoot.left == None:
                        leftNode = Node(data)
                        tempRoot.left = leftNode
                        break
                    tempRoot = tempRoot.left
                else:
                    if tempRoot.right == None:
                        rightNode = Node(data)
                        tempRoot.right = rightNode
                        break
                    tempRoot = tempRoot.right

        return self.root
    
    def breadFirst(self,root):
        bfQueue = Queue()
        self.queue.enQueue(root)
        while self.queue.isEmpty() != True:
            n = self.queue.deQueue()
            bfQueue.enQueue(n)
            travel = n
            if travel.left != None:
                self.queue.enQueue(travel.left)
            if travel.right != None:
                self.queue.enQueue(travel.right)
        print("Breadth : ",end='')
        bfQueue.printAll()
        print()

    def inOrder(self,root):
        if root!=None:
            self.inOrder(root.left)
            self.queue.enQueue(root)
            self.inOrder(root.right)
        if root == self.root:
            print("Inorder : ",end='')
            self.queue.printAll()
            print()

    def preOrder(self,root):
        if root != None:
            self.queue.enQueue(root)
            self.preOrder(root.left)
            self.preOrder(root.right)
        if root == self.root:
            print("Preorder : ",end='')
            self.queue.printAll()
            print()
    
    def postOrder(self,root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            self.queue.enQueue(root)
        if root == self.root:
            print("Postorder : ",end='')
            self.queue.printAll()
            print()

if __name__ == "__main__":
    inp = [int(i) for i in input('Enter Input : ').split()]
    tree = BiTree()
    for i in inp:
        root = tree.insert(i)

    tree.preOrder(root)
    tree.inOrder(root)
    tree.postOrder(root)
    tree.breadFirst(root)
