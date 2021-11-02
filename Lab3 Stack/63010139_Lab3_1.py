class Stack:
    def __init__(self):    # ใช้สำหรับสร้าง list ว่าง
        self.items =[]
        self.size_stack = 0
    def push(self,i):        # เก็บข้อมูลลง stack
        self.items.append(i)
        self.size_stack += 1
    def pop(self):          # นำข้อมูลออกจาก stack
        self.items.pop()
        self.size_stack -=1
    def isEmpty(self):   # ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        return self.size_stack == 0 
    def size(self):         # ตรวจสอบจำนวนข้อมูลใจ stack
        return self.size_stack

if __name__ == "__main__":
    print(" *** Stack implement by Python list***")
    
    ls = [e for e in input("Enter data to stack : ").split()]

    s = Stack()

    for e in ls:

        s.push(e)

    print(s.size(),"Data in stack : ",s.items)

    while not s.isEmpty():
        s.pop()

    print(s.size(),"Data in stack : ",s.items)
