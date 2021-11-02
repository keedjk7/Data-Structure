class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    # Code Here
    head = None 
    tail = None
    for i in LL :
        if head == None:
            head = Node(i)
        elif tail == None:
            tail = Node(i)
            head.next = tail
        else:
            newNode = Node(i)
            tail.next = newNode
            tail = newNode

    return head

def printLL(head):
    # Code Here
    txt = ""
    temp = head
    while temp != None :
        txt = txt + temp.value + " "
        temp = temp.next

    return txt

def SIZE(head):
    # Code Here
    count = 0
    temp = head
    while temp != None:
        count += 1
        temp = temp.next

    return count 

def scarmble(head, b, r, size):
    # Code Here
    tail = None
    rate_B = int((b/100)*size)
    rate_R = int((r/100)*size)
    find_tail = head

    while find_tail != None:
        tail = find_tail
        find_tail = find_tail.next
    for i in range (rate_B):
        temp = None
        if head.next != None:
            temp = head.next
            tail.next = head
            tail = head
            tail.next = None
            head = temp

    print("BottomUp {:.3f} % : {}".format(b,printLL(head)))
    ##########
    list1_head = head 
    list1_tail = None
    list2_head = None
    list2_tail = None

    count = head
    num = 0
    while count!= None:
        num +=1
        if num == rate_R:
            list1_tail = count
        if num - 1 == rate_R :
            list2_head = count
        if count.next == None:
            list2_tail = count
        count = count.next
    
    temp_list1 = list1_head.next
    temp_list2 = list2_head
    find_tail = head
    while temp_list1!=list2_head or temp_list2!=None:
        if temp_list2!=None:
            find_tail.next = temp_list2
            temp_list2 = temp_list2.next
            find_tail = find_tail.next
            find_tail.next = None
        if temp_list1!=list2_head:
            find_tail.next = temp_list1
            temp_list1 = temp_list1.next
            find_tail = find_tail.next
            find_tail.next = None

    print("Riffle {:.3f} % : {}".format(r,printLL(head)))
    ############
   
    num = 0
    count_forward = 1
    count_back = 1
    list1_head = head
    list1_tail = list1_head
    
    list2_head = head.next
    list2_tail = list2_head
    find_tail = list2_head.next
    
    list1_tail.next = None
    list2_tail.next = None

    while find_tail != None:
        num += 1
        if num % 2 == 1:
            if count_forward < rate_R :
                list1_tail.next = find_tail
                find_tail = find_tail.next
                list1_tail = list1_tail.next
                list1_tail.next = None
                count_forward += 1
            else:
                list2_tail.next = find_tail
                find_tail = find_tail.next
                list2_tail = list2_tail.next
                list2_tail.next = None
                count_back += 1
        else:
            if count_back < size - rate_R:
                list2_tail.next = find_tail
                find_tail = find_tail.next
                list2_tail = list2_tail.next
                list2_tail.next = None
                count_back += 1
            else :
                list1_tail.next = find_tail
                find_tail = find_tail.next
                list1_tail = list1_tail.next
                list1_tail.next = None
                count_forward += 1
            

    list1_tail.next = list2_head
    head = list1_head
    print("Deriffle {:.3f} % : {}".format(r,printLL(head)))
    ########################
    find_tail = head
    for i in range(size-rate_B-1):
        find_tail = find_tail.next
        tail = find_tail
    temp_head = head
    head = tail.next
    tail.next = None
    temp = head
    while temp.next!=None:
        temp = temp.next
    temp.next = temp_head

    print("Debottomup {:.3f} % : {}".format(b,printLL(head)))


inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":#case B before R
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":#case R before B
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)