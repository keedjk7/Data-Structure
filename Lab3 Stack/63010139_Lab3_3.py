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
    
    def infixToPostfix(self,inp):
        for c in inp:
            if c.isalpha() == True:   #Case Alphabet
                self.txt.append(c)
            elif c == '(' :  #Case (
                self.push(c)
            elif c == ')':  #Case )
                while (not self.isEmpty()) and (self.peek()!='('): # list not empty And top not ( 
                    p = self.pop()
                    self.txt.append(p)
                self.pop()
            else:           #Case Operator
                while(not self.isEmpty()) and (self.compareOperator(c)): #list not empty And check this operator
                    self.txt.append(self.pop())
                self.push(c)
        while not self.isEmpty():   # pop all the operatoer from list
            self.txt.append(self.pop())
        
if __name__ == "__main__":
    inp = input('Enter Infix : ')

    S = Stack()

    print('Postfix : ', end='')

    ### Enter Your Code Here ###

    S.infixToPostfix(inp)

    print(''.join(map(str,S.txt)))
    
    print()
