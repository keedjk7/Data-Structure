class Queue:
    def __init__ (self):
        self.list = []

    def enQueue(self,i):
        self.list.append(i)

    def deQueue(self):
        return self.list.pop(0)

    def size(self):
        return len(self.list)

if __name__ == "__main__":
    txt,time = input("Enter people and time : ").split()

    Q = Queue()
    cashier_A = Queue()
    cashier_B = Queue()
    time_A = 0 
    time_B = 0

    for e in txt:
        Q.enQueue(e)

    for minute in range (int(time)): 
        #pop
        if cashier_A.size() != 0 and  time_A % 3 == 0:
            temp_A = cashier_A.deQueue()
            time_A = 0
        if cashier_B.size() != 0 and time_B % 2 == 0:
            temp_B = cashier_B.deQueue()
            time_B = 0

        #push
        if Q.size() != 0:
            if cashier_A.size() != 5:
                cashier_A.enQueue(Q.deQueue())
            elif cashier_A.size() == 5 and cashier_B != 5:
                cashier_B.enQueue(Q.deQueue())

        #count down
        if cashier_A.size() != 0:
            time_A +=1
        if cashier_B.size() != 0:
            time_B +=1
       
        print(minute+1,Q.list,cashier_A.list,cashier_B.list)
