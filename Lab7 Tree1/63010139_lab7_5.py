class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Stack():
    def __init__(self):
        self.list = []
        
    def push(self, value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop() 

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return len(self.list) == 0

class BiTree():
    def __init__(self):
        self.root = None
        self.stack = Stack()
        self.txt_infix = ""
        self.txt_prefix = ""

    def insert(self,data):
        if data== '+' or data== '-' or data== '*' or data=='/':
            leftTemp = self.stack.pop()
            rightTemp =  self.stack.pop()
            newNode = Node(data)
            newNode.left = leftTemp
            newNode.right = rightTemp
            self.stack.push(newNode)
            
        else:
            newNode = Node(data)
            self.stack.push(newNode)
        
        return self.stack.peek()

    def infix(self,node):
        if node!=None:
            if node.data == '+' or node.data == '-' or node.data == '*' or node.data =='/':
                self.txt_infix += '('

            self.infix(node.right)
            self.txt_infix += str(node)
            self.infix(node.left)

            if node.data == '+' or node.data == '-' or node.data == '*' or node.data =='/':
                self.txt_infix += ')'
    
    def prefix(self,node):
        if node!=None:
            self.txt_prefix += str(node)
            self.prefix(node.right)
            self.prefix(node.left)

    def printTree(self,node,level = 0):
        if node != None:
            self.printTree(node.left,level+1)
            print('     ' * level, node)
            self.printTree(node.right,level+1)

if __name__ == "__main__":
    inp = input("Enter Postfix : ")
    tree = BiTree()
    for i in inp:
        root = tree.insert(i)
    print('Tree :')
    tree.printTree(root)
    print('--------------------------------------------------')
    tree.infix(root)
    print('Infix :',tree.txt_infix)
    tree.prefix(root)
    print('Prefix :',tree.txt_prefix)
