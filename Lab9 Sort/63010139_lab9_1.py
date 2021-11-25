def getMax(list,count):
    if len(list) <= 1:
        return list

    #swap [0] > [1]
    elif list[0] > list[1]:
        temp = list[0]
        list[0] = list[1]
        list[1] = temp
        return getMax(list,count)

    #recursive check sent reduce 1 size list 
    else:
        return [list[0]] + getMax(list[1:], count)

def bubble_sort(list,count):
    if count == len(list):
        return list
    
    list = getMax(list,count)
    return bubble_sort(list,count+1)

inp = [int(i) for i in input('Enter Input : ').split() ]


print(bubble_sort(inp,0))