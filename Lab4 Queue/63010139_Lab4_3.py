class Queue:
    def __init__(self):
        self.list = []

    def enQueue(self,i):
        self.list.append(i)

    def deQueue(self):
        return self.list.pop(0)

    def size(self):
        return len(self.list)

if __name__ == "__main__":
    txt,hint = input("Enter code,hint : ").split(",")
    
    move = ord(hint) - ord(txt[0])

    Q = Queue()

    for i in txt :
        Q.enQueue(chr(ord(i)+move))
        print(Q.list)