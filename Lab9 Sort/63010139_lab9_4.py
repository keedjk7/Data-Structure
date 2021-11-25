def partition(arr, low, high):
    i = (low-1)   
    pivot = arr[high]     
  
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
  
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  


l = [e for e in input("Enter Input : ").split()]

if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    temp_list = []

    list = []
    for i in l:
        list.append(int(i))
        temp_list.append(int(i))
        quickSort(temp_list,0,len(temp_list)-1)
        if len(list) == 1:
            print('list = {} : median = {:.1f}'.format(list,list[0]))
        elif len(list)%2 == 1:
            print('list = {} : median = {:.1f}'.format(list, temp_list[int(len(list)/2)] ))
        else:
            print('list = {} : median = {:.1f}'.format(list, (temp_list[int(len(list) / 2)] + temp_list[int((len(list) / 2) - 1)]) / 2  ))