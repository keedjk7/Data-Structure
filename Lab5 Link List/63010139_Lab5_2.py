class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        #Code Here
        if self.head == None:
            self.head = Node(item)
            self.head.next = None
            self.tail = self.head
        elif self.tail == self.head:
            self.tail = Node(item)
            self.head.next = self.tail
            self.tail.previous = self.head
            self.tail.next = None
        else:
            newNode = Node(item)            #NEW  T
            self.tail.next = newNode        #T->NEW
            newNode.previous = self.tail    #T-><-NEW
            newNode.next = None
            self.tail = newNode             #o-><-T

    def addHead(self, item):
        #Code Here
        if self.head == None:
            self.head = Node(item)
            self.next = None
            self.tail = self.head
        elif self.tail == None:
            self.tail = self.head
            self.head = Node(item)
            self.head.previous = None
            self.head.next = self.tail
            self.tail.previous = self.head
            self.tail.next = None
        else:
            newNode = Node(item)            #NEW    H
            self.head.previous = newNode    #NEW<-H
            newNode.next = self.head        #NEW-><-H
            newNode.previous = None    
            self.head = newNode             #H-><-o

    def insert(self, pos, item):
        #Code Here
        newNode = Node(item)
        count = 0
        if pos == 0 or pos <= (self.size()*-1) :
            self.addHead(item)
        elif pos == self.size() or pos >= self.size():
            self.append(item)
        elif pos >0: #case pose +
            node = self.head
            while node != None:
                if count == pos :
                    node_prev = node.previous       #New    P-><-NODE
                    node_prev.next = newNode        #P->New     P<-NODE
                    newNode.previous = node_prev    #P-><-New   P<-NODE  
                    newNode.next = node             #P-><-New->NODE
                    node.previous = newNode         #P-><-New-><-NODE 
                    break
                count += 1
                node = node.next

        else:       #case pose -
            node = self.tail
            while node != None:
                if count == pos :
                    node_next = node.next           #New    Node-><-x
                    node_next.previous = newNode    #New<-x Node->x
                    newNode.next = node_next        #New-><-x   Node->x
                    node.next = newNode             #Node->New-><-x
                    newNode.previous = node         #Node-><-New-><-x
                    break
                count -= 1
                node = node.previous


    def search(self, item):
        #Code Here
        status = "Not Found"
        if self.size != 0:       
            node = self.head
            if self.head == self.tail and self.head.value == item:
                status = "Found"
            else:
                count = 0
                while node != None:
                    if node.value == item:
                        status = "Found"
                        break
                    else:
                        count += 1
                        node = node.next

        return status

    def index(self, item):
        #Code Here
        found_at = -1
        if self.size != 0:       
            node = self.head
            if self.head == self.tail and self.head.value == item:
                found_at = 0
            else:
                count = 0
                while node != None:
                    if node.value == item:
                        found_at = count
                        break
                    else:
                        count += 1
                        node = node.next

        return found_at

    def size(self):
        #Code Here
        node = self.head
        count = 0
        if self.head == None and self.tail == None:
            return 0
        elif self.head == self.tail:
            return 1
        else:
            while node!=None:
                count +=1
                node = node.next
            return count

    def pop(self, pos):
        #Code Here
        POP = False
        count = 0
        if self.size() == 1 and pos == 0: #case have list 1
            self.head = None
            self.tail = None
            POP = True
        elif ((pos == self.size()-1  or pos == -1) and self.size()!=0): #case pop tail
            if self.size() >2:
                self.tail = self.tail.previous  #T-><-o
                self.tail.next = None           #T
            else:
                self.head.next = None
                self.tail = self.head

            POP = True
        elif ((pos == 0  or pos == self.size()* -1 ) and self.size() !=0): #case pop head
            if self.szie() > 2:
                self.head  = self.head.next     #o-><-H
                self.head.previous = None       #H
            else:
                self.head = self.tail
                self.head.previous = None
                self.tail = self.head

            POP = True

        elif pos > 0:       #case pos +
            node = self.head
            while node!= None :
                if  count == pos and node != self.tail:
                    prev_node = node.previous       #P-><-Node-><-x
                    next_node = node.next
                    prev_node.next = next_node      #P->x   P<-Node-><-x
                    next_node.previous = prev_node  #P-><-x 
                    POP = True
                    break
                count +=1
                node = node.next               

        elif pos < 0:       #case pos -
            node = self.tail
            count = -1
            while node != None :
                if count == pos and node != self.head:
                    prev_node = node.previous       #P-><-Node-><-x
                    next_node = node.next
                    prev_node.next = next_node      #P->x   P<-Node-><-x
                    next_node.previous = prev_node  #P-><-x 
                    POP = True
                    break
                count -= 1
                node = node.precious

        if POP == False:
            return "Out of Range"
        else:
            return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())