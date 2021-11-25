class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binaryTree():
    def __init__(self):
        self.root = None
        self.level = 0

    def insert(self,data):
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
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

    def inorder_check(self,node,number_check):
        if node!= None:
            self.inorder_check(node.left,number_check)
            if node.data <= number_check:
                self.level += 1
            self.inorder_check(node.right,number_check)


if __name__ == '__main__':
    inp = [e for e in input("Enter Input : ").split("/")]

    list_number = []

    for i in inp[0].split(' '):
        list_number.append(int(i))

    number_check_level = int(inp[1])

    tree = binaryTree()
    for i in list_number:
        root = tree.insert(i)

    tree.printTree(root)

    tree.inorder_check(root,number_check_level)
    print('--------------------------------------------------')
    print('Rank of {} : {}'.format(number_check_level,tree.level))

