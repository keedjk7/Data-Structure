class Stack:
    def __init__(self):
        self.list = []
        self.top = -1
        self.size = 0

    def push(self,i):
        self.list.append(i)
        self.top = self.list[-1]
        self.size += 1

    def pop(self):
        temp = self.top
        self.list.pop()
        if len(self.list)>=1:
            self.top = self.list[-1]
            
        else:
            self.top = None

        self.size -= 1
        return temp

    def isEmpty(self):
        return len(self.list) == 0

    def peek(self):
        return self.top

if __name__ == "__main__":
    print("******** Parking Lot ********")

    m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
    #m = max , s = in Soi , o = status , n = car in status 

    m,n = int(m),int(n)

    ### Enter Your Code Here ###

    A = Stack()
    B = Stack()
    car_status = ["Out"] * (m*2)
    
    #put car in Soi to A
    for f in range(len(s)):
        i = s[f]
        if (i!=',')== True:
            number = int(s[f])
            if number != 0:
                A.push(number)
                car_status[number-1] = "In"

    #process car status
    found = False
    temp = -1
    if (o == "arrive") == True: #arrive
        #print(A.size,m,car_status)
        if (A.size == m) == True:
            print("car",n,"cannot arrive : Soi Full")
        elif (car_status[n-1] == "Out") == True :
            A.push(n)
            car_status[n-1] = "In"
            print("car",n,"arrive! : Add Car",n)
        else:
            print("car",n,"already in soi")

    elif (o == "depart") == True:  #depart
        if(A.size == 0) == True:
            print("car",n,"cannot depart : Soi Empty")
        elif (car_status[n-1] == "In") == True:
            while found == False: #find
                if (A.top == n) == True:
                    found = True
                    temp = A.pop()
                    car_status[n-1] = "Out"
                else:
                    B.push(A.pop())
            while B.isEmpty()!= True:
                A.push(B.pop())
            print("car",n,"depart ! : Car",n,"was remove")
        else:
            print("car",n,"cannot depart : Dont Have Car",n)

    print(A.list)
