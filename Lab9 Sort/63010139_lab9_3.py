def swap(list,count,last,last_number):
    if count < 0:
        return list,last
    else:
        list,position = swap(list,count-1,last,last_number)
        
        if list[last] < list[count]:
            if list[last] == last_number:
                position = count
            temp = list[last]
            list[last] = list[count]
            list[count] = temp

        return list,position


def insert(list,count):
    if count == 0:
        return list
    else:
        list = insert(list,count-1)
        last = count
        last_number = list[last]
        list,position = swap(list,count,last,last_number)

        print('insert {} at index {} : '.format(last_number,position),end='')
        
    if len(list[count+1:]) == 0:
        print(list[:count+1])
    else:
        print(list[:count+1],list[count+1:])
        
    return list
    

inp = [int(i) for i in input('Enter Input : ').split()]


list = insert(inp,len(inp)-1)
print('sorted')
print(list)