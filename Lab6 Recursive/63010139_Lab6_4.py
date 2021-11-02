class stack:
    def __init__(self,chr):
        self.list = []
        self.chr = chr
        self.size = 0

    def push(self,i):
        self.list.append(i)
        self.size += 1
    def pop(self):
        self.size -= 1
        return self.list.pop()

def check(A,B,C,number,total):
    if A.size <= total:
        print('|',end="  ")
    else:
        print(A.list[total],end="  ")
    
    if B.size <= total:
        print('|',end="  ")
    else:
        print(B.list[total],end="  ")
    
    if C.size <= total:
        print('|')
    else:
        print(C.list[total])
    

def show(number,temp,A,B,C):

    if temp == 0:
        check(A,B,C,temp-1,number-temp)
    else:
        show(number,temp-1,A,B,C)
        check(A,B,C,temp,number-temp)
    
    return temp+1

def TowerOfHanoi(number,count , source, destination, auxiliary):
    if count==1:
        destination.push(source.pop())
        print("move {} from  {} to {}".format(count,source.chr,destination.chr))
        show(number,number,A,B,C)
        return
    TowerOfHanoi(number,count-1, source, auxiliary, destination)
    destination.push(source.pop())
    print("move {} from  {} to {}".format(count,source.chr,destination.chr))
    show(number,number,A,B,C)
    TowerOfHanoi(number,count-1, auxiliary, destination, source)
          
def put_inp(count,number,A):
    if number == count:
        A.push(number)
    else:
        A.push(put_inp(count+1,number,A))
    
    return count-1
    

number = int(input("Enter Input : "))
A = stack('A')
B = stack('B')
C = stack('C')
put_inp(1,number,A)


show(number,number,A,B,C)
TowerOfHanoi(number,number,A,C,B) 