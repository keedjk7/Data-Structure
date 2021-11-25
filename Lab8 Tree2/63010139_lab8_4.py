class node():
    def __init__(self,position,power):
        self.power = power
        self.position = position
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.position)

class Queue():
    def __init__(self):
        self.list = []
    
    def enQueue(self,data):
        self.list.append(data)

    def deQueue(self):
        return self.list.pop(0)

    def isEmpty(self):
        return len(self.list) == 0

class binaryTree():
    def __init__(self):
        self.root = None
        self.queue = Queue()
        self.keep = []

    def createTree(self,list_power):
        tempNode = None
        for i in range(len(list_power)):
            if self.root == None:
                newNode = node(i,list_power[i])
                self.root = newNode
                self.queue.enQueue(newNode)
                self.keep.append(newNode)

            elif self.queue.isEmpty() == False:
                if tempNode == None or tempNode.right != None:
                    tempNode = self.queue.deQueue()
                    newNode = node(i,list_power[i])
                    tempNode.left = newNode
                    self.queue.enQueue(newNode)
                    self.keep.append(newNode)
                else:
                    newNode = node(i,list_power[i])
                    tempNode.right = newNode
                    self.queue.enQueue(newNode)
                    self.keep.append(newNode)
        
        return self.root

    def compare_power(self,position1,position2):
        power_position1 = self.keep[position1].power
        if self.keep[position1].left != None:
            power_position1 += self.keep[position1].left.power
        if self.keep[position1].right != None:
            self.keep[position1].right.power

        power_position2 = self.keep[position2].power
        if self.keep[position2].left != None:
            power_position2 += self.keep[position2].left.power
        if self.keep[position2].right != None:
            self.keep[position2].right.power

        if power_position1 > power_position2:
            return '{}>{}'.format(position1,position2)
        elif power_position1 < power_position2:
            return '{}<{}'.format(position1,position2)
        else:
            return '{}={}'.format(position1,position2)

        
            
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == '__main__':
    power,order_compare = input('Enter Input : ').split('/')

    list_power = []
    list_order = []
    total_power = 0

    for i in power.split(' '):
        list_power.append(int(i))
        total_power += int(i)

    for i in order_compare.split(','):
        list_order.append(i)

    list_first_position_order = []
    list_second_position_order = []
    
    for i in list_order:
        for j in i.split(' '):
            if len(list_first_position_order) == len(list_second_position_order):
                list_first_position_order.append(int(j))
            else:
                list_second_position_order.append(int(j))
         
        

    print(total_power)
    
    tree = binaryTree()
    root = tree.createTree(list_power)
    #tree.printTree(root)
    for i in range (len(list_first_position_order)):
        print(tree.compare_power(list_first_position_order[i],list_second_position_order[i]))
