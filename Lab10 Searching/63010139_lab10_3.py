class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    # Code Here
    def __init__(self, size, maxCollision):
        self.size = size
        self.maxCollision = maxCollision
        self.table=[]
        for i in range(size):
            self.table.append(None)

    def __str__(self):
        text = ""
        for i in range(len(self.table)):
            text = text + "#" + str(i+1) + "      " + str(self.table[i]) + "\n"
        return text

    def insert(self,key,value):
        originalkeySum = 0
        for i in key:
            originalkeySum += ord(i)
        collisionCounter = 0
        keySum = originalkeySum
        while True:
            if collisionCounter == self.maxCollision:
                print("Max of collisionChain")
                return
            if self.table[keySum%self.size] is not None:
                collisionCounter += 1
                print("collision number {} at {}".format(collisionCounter, (keySum%self.size)))
                keySum = originalkeySum + collisionCounter * collisionCounter
            else:
                self.table[keySum % self.size] = Data(key,value)
                break

    def isFull(self):
        check = 0
        for i in self.table:
            if i is not None:
                check += 1
        return check == self.size

if __name__ == "__main__":
    print(" ***** Fun with hashing *****")
    inp = input("Enter Input : ").split("/")
    size, maxCollision = inp[0].split(" ")
    size = int(size)
    maxCollision = int(maxCollision)
    inp[1] = inp[1].split(",")
    h = hash(size,maxCollision)
    for i in inp[1]:
        if (h.isFull()):
            print("This table is full !!!!!!")
            break
        key,value = i.split(" ")
        h.insert(key, value)
        print(h, end = "")
        print("---------------------------")