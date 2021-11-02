import re
class Node:
    def __init__(self, data = None,index = None):
        self.data = data
        self.index = index
        self.next = None
    def __repr__(self):
        return self.data
    

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return self.show()

    def show(self):
        temp = self.head
        list = []
        txt_show = "link list : "
        while temp != None:
            list.append(temp.data)
            temp = temp.next
        for e in list :
            if e != list[0]:
                txt_show = txt_show + "->" 
            txt_show = txt_show + str(e)

        if txt_show == "link list : ":
            return "List is empty"
        else:
            return txt_show

    def isEmpty(self):
        temp = self.head
        count = 0
        while temp != None :
            count +=1
            temp = temp.next

        return count == 0
    
    def append(self,data):
        temp = Node(data,data)
        if self.head == None:
            self.head = Node(temp)
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = Node(temp)
        
    def insert(self,index,data):
        find = False
        node = self.head
        count_index = 0

        if int(index) == 0: #dummy
            newNode = Node(data,index)
            self.head = newNode
            self.head.next = node
            find = True
        else:
            while node != None:
                if count_index == int(index)-1 or (node.next == None and int(index)-1 == count_index):
                    newNode = Node(data,index)
                    newNode.next = node.next
                    node.next = newNode
                    find = True
                    break

                node = node.next
                count_index += 1

        return find

if __name__ == "__main__":
    inp = input("Enter Input : ")
    txt = re.split(', |,',inp)

    list_temp = []

    for e in txt :
        if (e == txt[0]) ==True:
            for i in txt[0].split(' '):
                list_temp.append(i)

            l_list = LinkedList()
    
            for e in list_temp :
                if e != '':
                    l_list.append(e)
            
            print(l_list)

        else:
            index = None
            data = None
            for number in e.split(':'):
                if index != None :
                    data = number
                else:
                    index = number   
            
            can_insert = False       
            if int(index) >=0:
                can_insert = l_list.insert(index,data)

            if can_insert == False  :
                print("Data cannot be added")
                print(l_list)
            else:
                print("index =",index,"and data =",data)
                print(l_list)


        