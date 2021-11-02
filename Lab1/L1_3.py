print("*** Election ***")
number_vote = int(input("Enter a number of voter(s) : "))

count_vote =[]

count_vote[:20] = [0] * 20

check = False
max = 0
equal = False
position = 0

temp = input().split()

for i in range(number_vote) :
    if (check == False and (int(temp[i]) > 0 and int(temp[i]) <= 20)) :
        check =True
    if int(temp[i]) > 0 and int(temp[i]) <= 20 :
        count_vote[int(temp[i]) - 1] += 1
        if(count_vote[int(temp[i]) - 1] > max) :
            max = count_vote[int(temp[i]) - 1]
            position = int(temp[i])
            equal = False
        elif(count_vote[int(temp[i]) - 1] == max) :
            equal = True
        elif(count_vote[int(temp[i]) - 1] < max) :
            equal = False

if check == False or equal == True  :
    print("*** No Candidate Wins ***")
else :
    print(position)
    