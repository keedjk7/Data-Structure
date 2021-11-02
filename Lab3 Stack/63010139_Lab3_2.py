class Stack:
    def __init__ (self):
        self.list = []
        self.top = -1
        self.size_stack = 0

    def push(self,i):
        self.list.append(i)
        self.top = self.list[-1]
        self.size_stack +=1

    def pop(self):
        self.list.pop()
        if(self.size_stack > 1):
            self.top = self.list[-1]
        else:
            self.top = -1
        self.size_stack -=1

    def isEmpty(self):
        return self.size_stack == 0

    def checkTop(self):
        return self.top

    def clear(self):
        self.list.clear()
        self.size_stack = 0


if __name__ == "__main__":
    txt = input("Enter expresion : ")

    S = Stack()
    match = False
    
    for f in range(len(txt)):
        i = txt[f]
        if i == '(' or i == '[' or i == '{': #case ( [ {
            S.push(i)
        elif i == ')': # case )
            if S.checkTop() == '(':
                S.pop()
                if(f == len(txt)-1 and S.isEmpty() == True):
                    match = True
            elif S.isEmpty() == True:
                print(txt,"close paren excess")
                break;
            else:
                print(txt,"Unmatch open-close")
                S.clear()
                break

        elif i == ']' : #case ]
            if S.checkTop() == '[':
                S.pop()
                if(f == len(txt)-1 and S.isEmpty() == True):
                    match = True
            elif S.isEmpty() == True:
                print(txt,"close paren excess")
                break
            else:
                print(txt,"Unmatch open-close")
                S.clear()
                break

        elif i =='}': #case }
            if S.checkTop() == '{':
                S.pop()
                if(f == len(txt)-1 and S.isEmpty() == True):
                    match = True
            elif S.isEmpty() == True:
                print(txt,"close paren excess")
                break
            else:
                print(txt,"Unmatch open-close")
                S.clear()
                break

    if S.isEmpty() == False:  #case open
        print(txt,"open paren excess  ",S.size_stack,":",''.join(map(str,S.list)))
    elif match == True:
        print(txt,"MATCH")
                
        
