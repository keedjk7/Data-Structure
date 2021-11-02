import re
class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
        self.data = data
        self.next = next
    def __str__(self):
        ### Code Here ###
        return self.data

def createList(l=[]):
    ### Code Here ###
    head = None
    temp = None
    for e in l:
        if head == None:
            head = node(int(e),None)
            temp = head
        else:
            newNode = node(int(e),None)
            temp.next = newNode
            temp = newNode

    return head

def printList(H):
    ### Code Here ###
    txt = ""
    while H!=None:
        txt = txt + str(H.data)+" "
        H = H.next
    print(txt)

def mergeOrderesList(p,q):
    ### Code Here ###
    head = None
    tail = None
    while p!=None :
        if head == None:
            head = node(p.data,None)
        else:
            check = head
            while check!=None:
                if tail == None:
                    newNode = node(p.data,None)
                    tail = newNode
                    head.next = tail
                    break
                elif check.next == tail and p.data >= check.data: #check at tail and >=
                    newNode = node(p.data,None)
                    tail.next = newNode
                    tail = newNode
                    break 
                elif check.next ==None and p.data <= check.next.data and p.data >=check.data: #check not at tail,insert at head
                    newNode =node(p.data,check)
                    head = newNode
                    break
                check = check.next

            if check == None and p.data < head.data :#insert head
                newNode = node(p.data,head)
                head = newNode
        p = p.next

    

    while q!=None :
        
        if head == None:
            head = node(q.data,None)
        else:
            check = head
            while check!=None:
                if tail == None:  
                    newNode = node(q.data,None)
                    tail = newNode
                    head.next = tail
                    break
                elif check.next == tail and q.data > tail.data: #check at tail and >
                    newNode = node(q.data,None)
                    tail.next = newNode
                    tail = newNode
                    break 
                elif check.next!=None and q.data <= check.next.data and q.data>=check.data : #check not at tail,insert after
                    nextNode = check.next 
                    newNode =node(q.data,nextNode)
                    check.next = newNode
                    break
                check = check.next

            if check == None and q.data < head.data :#insert head
                newNode = node(q.data,head)
                head = newNode

        q = q.next 

    return head
#################### FIX comand ####################   
# input only a number save in L1,L2
inp1,inp2 = input("Enter 2 Lists : ").split(' ')

L1 =[]
for i in inp1.split(','):
    L1.append(int(i))
L2=[]
for i in inp2.split(','):
    L2.append(int(i))

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)