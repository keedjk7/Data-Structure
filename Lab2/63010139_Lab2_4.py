def check_equal(show_list,temp):
    if len(show_list)>0:
        list2 = sorted(temp)
        for i in range (len(show_list)):
            list1 = sorted(show_list[i])
            if list1 == list2 :
                list1.clear()
                return False
    return True
        
def find_array(list_number):
    show_list = []
    Size = len(list_number)
    for i in range (Size-2):
        for j in range(i+1,Size-1):
            for k in range(j+1,Size):
                temp = []
                
                if list_number[i]+list_number[j]+list_number[k] == 0 :
                    temp.append(list_number[i])
                    temp.append(list_number[j])
                    temp.append(list_number[k])
                    show_list.append
                    
                    
                    check = check_equal(show_list,temp)
                    if check == True :
                        show_list.append(temp)
                    

    return show_list

if __name__ == "__main__":
    list_number = input("Enter Your List : ").split()
    
    list_number = list(map(int, list_number))

    if len(list_number) > 2:
        print(find_array(list_number))
    else :
        print("Array Input Length Must More Than 2")
        