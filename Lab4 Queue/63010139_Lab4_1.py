class Queue:
    def __init__ (self):
        self.list = []

    def enQueue (self,i):
        self.list.append(i)

    def deQueue(self):
        return self.list.pop(0)

    def size(self):
        return len(self.list)

ls = [e for e in input("Enter Input : ").split(",")]

Q = Queue()

status = "None"

for e in ls:
    for i in e.split():
        if i.isdigit() and (status == "Push") == True:
            Q.enQueue(i)
            status = "None"
            print(Q.size())
        elif i == 'E':
            status = "Push"
        elif i == 'D' :
            if Q.size() == 0 :
                print("-1")
            else:
                print(Q.deQueue(),"0")

if Q.size() == 0:
    print("Empty")
else:
    print(' '.join(Q.list))