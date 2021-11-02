class Stack:

    def __init__(self):
        self.list = []
        self.txt = []
        self.size_list = 0
        self.precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
        
    def push(self, value):
        self.size_list += 1
        self.list.append(value)
        
    def pop(self):
        self.size_list -= 1
        return self.list.pop() 

    def show(self):
        return self.txt()
        
    def peek(self):  # top element in list
        return self.list[-1]

    def isEmpty(self):
        return self.size_list == 0
    
    def compareOperator(self,c):
        try:
            a = self.precedence[c] 
            b = self.precedence[self.peek()]
            return a<=b
        except KeyError:
            return False
def infix2postfix(inp):
     S = Stack()
     for c in inp:
        if c.isalpha() == True:   #Case Alphabet
             S.txt.append(c)
        elif c == '(' :  #Case (
               S.push(c)
        elif c == ')':  #Case )
            while (not S.isEmpty()) and (S.peek()!='('): # list not empty And top not ( 
                p = S.pop()
                S.txt.append(p)
            S.pop()
        else:           #Case Operator
            while(not S.isEmpty()) and (S.compareOperator(c)): #list not empty And check this operator
                S.txt.append(S.pop())
            S.push(c)
     while not S.isEmpty():   # pop all the operatoer from list
        S.txt.append(S.pop())

     output = "" 
     
     for i in S.txt: 
        output += i 
    
     return output
    
        
if __name__ == "__main__":
    print(" ***Infix to Postfix***")

    token = input("Enter Infix expression : ")

    print("PostFix : ")

    print(infix2postfix(token))
