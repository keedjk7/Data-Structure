class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BiTree():
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

    def searchAll(self,node,k):
        if node != None:
            self.searchAll(node.right,k)
            if node.data > k:
                node.data *= 3
            self.searchAll(node.left,k)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)           
            self.printTree(node.left, level + 1)


if __name__ == "__main__":
    inp, k = input('Enter Input : ').split('/')
    list = []
    for i in inp.split(' '):
        list.append(int(i))

    tree = BiTree()

    for i in list:
        root = tree.insert(i)

    tree.printTree(root)
    tree.searchAll(root,int(k))
    print("--------------------------------------------------")
    tree.printTree(root)
