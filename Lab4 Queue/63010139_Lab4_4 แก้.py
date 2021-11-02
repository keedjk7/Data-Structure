class Queue:
    def __init__(self):
        self.list = []
        self.act_place = []

    def enQueue(self,Str,i):
        if (Str == "List") == True:
            self.list.append(i)
        else:
            self.act_place.append(i)

    def deQueue(self,Str):
        if (Str == "List") == True:
            return self.list.pop(0)

    def size(self):
        return len(self.list)

def check_act(activity):
    if activity == 0:
        return "Eat"
    elif activity == 1:
        return "Game"
    elif activity == 2:
        return "Learn"
    elif activity == 3:
        return "Movie"

def check_place(place):
    if place == 0:
        return "Res."
    elif place == 1:
        return "ClassR."
    elif place == 2:
        return "SuperM."
    elif place == 3:
        return "Home"

def check_love_score(act1,act2,place1,place2):
    if (act1 == act2) == True and (place1 == place2) == True:
        return 4
    elif (act1 == act2) == True:
        return 1
    elif (place1 == place2) == True:
        return 2
    else:
        return -5

if __name__ == "__main__":
    txt = input("Enter Input : ").split(",")

    myQueue = Queue()
    yourQueue = Queue()

    count = 0
    love_score = 0
    
    for e in txt :
        for i in e.split():
            count +=1
            if count %2 == 1:
                    myQueue.enQueue("List",i)
            else:
                    yourQueue.enQueue("List",i)
                    
    print("My   Queue =",', '.join(myQueue.list))
    print("Your Queue =",', '.join(yourQueue.list))

    while myQueue.size() != 0 and yourQueue.size() != 0:
        temp1 = myQueue.deQueue("List")
        act1 = check_act(int(temp1[0]))
        place1 = check_place(int(temp1[2]))
        sent1 = str(act1)+":"+ str(place1)
        myQueue.enQueue("",sent1)
        
        temp2 = yourQueue.deQueue("List")
        act2 = check_act(int(temp2[0]))
        place2 = check_place(int(temp2[2]))
        sent2 = str(act2)+":"+str(place2)
        yourQueue.enQueue("",sent2)

        love_score +=check_love_score(act1,act2,place1,place2)
        
    print("My   Activity:Location =",', '.join(myQueue.act_place))
    print("Your Activity:Location =",', '.join(yourQueue.act_place))
    if love_score >=7 :
        print("Yes! You're my love! : Score is "+str(love_score)+".")
    elif love_score<7 and love_score > 0 :
        print("Umm.. It's complicated relationship! : Score is "+str(love_score)+".")
    else:
        print("No! We're just friends. : Score is "+str(love_score)+".")
