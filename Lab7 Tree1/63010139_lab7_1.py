class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        if self.root == None:
            self.root = Node(data)
        else:
            tempRoot = self.root
            while tempRoot!=None:
                if data<tempRoot.data:
                    if tempRoot.left == None:
                        leavesNode = Node(data)
                        tempRoot.left = leavesNode
                        break
                    tempRoot = tempRoot.left
                else:
                    if tempRoot.right == None:
                        leavesNode = Node(data)
                        tempRoot.right = leavesNode
                        break
                    tempRoot = tempRoot.right

        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
