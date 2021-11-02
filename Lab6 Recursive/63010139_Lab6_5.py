# def inside_positive(count1,count2):
#     txt = ""
    
#     if count2 == number:
#         return "\n"
#     txt += inside_positive(count1,count2+1)
#     if count1 <= number-2-count2:
#         return "_"+txt
#     else:
#         return "#"+txt   
    
# def positive(count1,number):
#     txt = ""
#     if count1 == number:
#         return ""
#     txt += inside_positive(count1,0)
#     txt += positive(count1+1,number)

#     return txt

# def inside_negative(count1,count2):
#     txt = ""

#     if count2 == number:
#         return "\n"
#     txt += inside_negative(count1,count2+1)
#     if count1 <= count2:
#         return "#"+txt
#     else:
#         return "_"+txt

# def negative(count1,number):
#     txt = ""
#     if count1 == number:
#         return ""
#     txt += inside_negative(count1,0)
#     txt += negative(count1+1,number)

#     return txt

# def staircase(n):
#     global number
#     number = n
#     if number == 0:
#         return "Not Draw!"
#     elif number>0:
#         return positive(0,number)
#     else:
#         number *= -1
#         return negative(0,number)

# print(staircase(int(input("Enter Input : "))))
def staircase(n, x):
    if n == 0:
        print("Not Draw!")
    elif n > 0:
        if n == 1:
            print("_"*(n-1), end='')
            print("#"*x)
            return
        print("_"*(n-1), end='')
        print("#"*x)
        n = n-1
        x = x+1
        staircase(n,x)
    elif n < 0:
        if n == -1:
            print("_"*(x-1), end='')
            print("#"*abs(n))
            return
        print("_"*(x-1), end='')
        print("#"*abs(n))
        n = n+1
        x = x+1
        staircase(n, x)


n = input("Enter Input : ")
n = int(n)
staircase(n,1)