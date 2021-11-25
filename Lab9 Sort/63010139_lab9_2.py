
def bubble_sort(list):

    for i in range (0,len(list)-1,1):
        for j in range (i+1,len(list),1):
            if list[i] > list[j] and list[i] >= 0 and list[j] >= 0:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            

    return list

inp = [int(i) for i in input('Enter Input : ').split() ]


inp = bubble_sort(inp)
for i in inp:
    print(i,end=' ')