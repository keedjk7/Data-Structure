number = int(input("Enter Input : "))

line = ((number+1)*2)+2

array = [ [ 'x' ] * line ] * line

for i in range (line) :
    for j in range(line) :

        
        # print .
        if j<=line/2-2-i or i >= line-j+(line/2) :
            print(".", end="")
        # print dot +
        elif (i>=line-1-number and i<=line-2) and (j>=1 and j<=number ) :
            print("+", end="")
        #print dot #
        elif (i>=1 and i<=number) and (j>=line-1-number and j<=line-2 ) :
            print("#", end="")
        #print general #
        elif j < line / 2 :
            print("#", end="")
        else :
            print("+", end="")
    print("")
