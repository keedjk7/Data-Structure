class Stack:
    def __init__ (self):
        self.stack = []
        self.count = []

    def push(self,i):
        self.stack.append(i)

    def pop(self):
        return self.stack.pop()

    def push_count(self,i):
        self.count.append(i)

    def pop_count(self):
        return self.count.pop()

    def size_stack(self):
        return len(self.stack)

    def size_count(self):
        return len(self.count)

class Queue:
    def __init__(self):
        self.queue = []

    def enQueue(self,i):
        self.queue.append(i)

    def deQueue(self):
        return self.queue.pop(0)

    def size_queue(self):
        return len(self.queue)

def reverse(Str):
    return Str[::-1]


if __name__ == "__main__":
    normal_inp,mirror_inp = input("Enter Input (Normal, Mirror) : ").split()

    mirror_S = Stack()
    mirror_Q = Queue()
    mirror_inp = reverse(mirror_inp)

    mirror_keep = ""
    mirror_bomb = 0

    
    
    for e in mirror_inp :
        mirror_S.push(e)
        count_mirror = 0
        if mirror_S.size_count()!=0 :
            count_mirror = mirror_S.pop_count()

        if (e == mirror_keep) == True:  #Same chr
            count_mirror +=1
            mirror_S.push_count(count_mirror)
        else:                           #not Same chr
            mirror_keep = e
            mirror_S.push_count(count_mirror)
            mirror_S.push_count(0)

        if count_mirror == 2:       #Same 3 chr Bomb!
            mirror_Q.enQueue(mirror_keep)
            for i in range(3):
                P = mirror_S.pop()

            mirror_count_chr = 0
            mirror_bomb += 1
            C = mirror_S.pop_count()
            
            if mirror_S.size_stack() == 0:    #mirror Stack empty
                mirror_keep = ""
            else:                           #mirror Stack not empty
                mirror_keep = mirror_S.pop()
                mirror_S.push(mirror_keep)

        
      
    normal_S = Stack()
    normal_Q = Queue()

    normal_keep = ""
    normal_count_chr = 0
    normal_bomb = 0
    normal_fail_bomb = 0
    
    for e in normal_inp :
        normal_S.push(e)
        count_normal = 0
        if normal_S.size_count()!= 0 :
            count_normal = normal_S.pop_count()

        if (e == normal_keep) == True:
            count_normal += 1
            normal_S.push_count(count_normal)
        else:
            normal_keep = e
            normal_S.push_count(count_normal)
            normal_S.push_count(0)


        if count_normal == 2:   #same 3 chr
            if mirror_Q.size_queue()!= 0:     # Q from mirror not empty
                temp_mir = mirror_Q.deQueue()
                temp_nor = normal_S.pop()
                normal_S.push(temp_mir)
                if (temp_mir == normal_keep) == True:   #insert then same
                    normal_Q.enQueue(normal_keep)
                    for i in range (3):
                        P = normal_S.pop()
                    normal_S.push(temp_nor)
                    normal_fail_bomb += 1
                    normal_keep = temp_nor
                    C = normal_S.pop_count()
                    normal_S.push_count(0)
                else:                               #insert then not same
                    normal_S.push(temp_nor)
                    temp = normal_S.pop_count()
                    normal_S.push_count(temp-1)
                    normal_S.push_count(0)
                    normal_S.push_count(0)
                    normal_keep = temp_nor
            else:                       # Q from mirror empty
                normal_Q.enQueue(normal_keep)
                for i in range (3):
                    P = normal_S.pop()
                normal_count_chr = 0
                normal_bomb += 1
                if normal_S.size_stack()!=0:
                    temp_nor = normal_S.pop()
                    normal_S.push(temp_nor)
                    normal_keep = temp_nor
                else:
                    normal_keep = ""
                C = normal_S.pop_count()

    print("NORMAL :")
    print(normal_S.size_stack())
    if normal_S.size_stack() == 0:
        print("Empty")
    else:
        show_normal = ""
        for i in range (normal_S.size_stack()):
            show_normal = show_normal + normal_S.stack[i]
        show_normal = reverse(show_normal)
        print(show_normal)

    print(normal_bomb,"Explosive(s) ! ! ! (NORMAL)")
    if normal_fail_bomb != 0:
        print("Failed Interrupted",normal_fail_bomb,"Bomb(s)")

    print("------------MIRROR------------")
    print(": RORRIM")
    print(mirror_S.size_stack())
    if mirror_S.size_stack() == 0:
        print("ytpmE")
    else:
        show_mirror = ""
        for i in range (mirror_S.size_stack()):
            show_mirror = show_mirror + mirror_S.stack[i]
        show_mirror = reverse(show_mirror)
        print(show_mirror)
    print("(RORRIM) ! ! ! (s)evisolpxE",mirror_bomb)

                    
            

    

    
