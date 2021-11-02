class node:
    def __init__(self,prev,next,data):
        self.prev = prev
        self.next = next
        self.data = data

class DB_LinkList:
    def __init__(self):
        self.cursor = node(None,None,'|')
        self.head = self.cursor
        self.tail = None
    
    def __str__(self):
        txt = ""
        e = self.head
        while e != None:
            txt = txt + e.data + " "
            e = e.next

        return txt

    def swap(self,node1,node2):
        temp = node1.data
        node1.data = node2.data
        node2.data = temp

    def insert(self,data):
        if self.tail == None:
            self.tail = node(self.head,None,data)
            self.head.next = self.tail
            self.swap(self.head,self.tail)
            self.cursor = self.tail
        elif self.tail == self.cursor:
            newNode = node(self.cursor,None,data)
            self.tail.next = newNode
            self.swap(newNode,self.tail)
            self.tail = newNode
            self.cursor = newNode
        else:
            newNode = node(self.cursor,self.cursor.next,data)
            self.cursor.next = newNode
            self.swap(self.cursor,newNode)
            self.cursor = newNode
    
    def move_left(self):
        if self.cursor.prev != None:
            self.swap(self.cursor.prev,self.cursor)
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor.next != None:
            self.swap(self.cursor,self.cursor.next)
            self.cursor = self.cursor.next

    def pop_left(self):
        if self.cursor.prev != None and self.cursor.prev.prev == None:
            self.cursor.prev = None
            self.head = self.cursor

        elif self.cursor.prev != None and self.cursor.prev.prev != None:
            newPrev = self.cursor.prev.prev
            newPrev.next = self.cursor
            self.cursor.prev = newPrev

    def pop_right(self):
        if self.cursor.next != None and self.cursor.next.next == None:
            self.cursor.next = None
            self.tail = self.cursor
        elif self.cursor.next != None and self.cursor.next.next != None:
            newNext = self.cursor.next.next
            newNext.prev =self.cursor
            self.cursor.next = newNext

if __name__ == "__main__":
    inp = input("Enter Input : ").split(',')
    LL = DB_LinkList()
    for e in inp:
        if e[:1] == 'I':
            LL.insert(e[2:])
        elif e[:1] == 'L':
            LL.move_left()
        elif e[:1] == 'R':
            LL.move_right()
        elif e[:1] == 'B':
            LL.pop_left()
        elif e[:1] == 'D':
            LL.pop_right()
    
    print(LL)