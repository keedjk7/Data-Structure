class football_team:
    def __init__(self):
        self.name = None
        self.wins = None
        self.loss = None
        self.draws = None
        self.scored = None
        self.conceded = None
        self.point = None
        self.gd = None
        self.allData = []

    def insert(self,list):
        self.name = list[0]
        self.wins = int(list[1])
        self.loss = int(list[2])
        self.draws = int(list[3])
        self.scored = int(list[4])
        self.conceded = int(list[5])
        self.cal_point()
        self.cal_gd()
        self.mergeAll()

    def cal_point(self):
        self.point = self.wins * 3 + self.draws * 1

    def cal_gd(self):
        self.gd = self.scored - self.conceded

    def mergeAll(self):
        self.allData.append(self.name)
        point = {}
        point["points"] = self.point
        self.allData.append(point)
        gd = {}
        gd["gd"] = self.gd
        self.allData.append(gd)

def sort(list):
    for i in range (len(list) - 1):
        for j in range (i+1, len(list), 1):
            if (list[i].point < list[j].point) or (list[i].point == list[j].point and list[i].gd < list[j].gd):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            
    
    return list

inp = (e for e in input('Enter Input : ').split('/'))

list = []

for i in inp:
    team = football_team()
    temp = []
    for j in i.split(','):
        temp.append(j)

    team.insert(temp)
    list.append(team)

print('== results ==')
list = sort(list)
for i in list:
    print(i.allData)