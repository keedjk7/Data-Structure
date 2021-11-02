def num_grid(lst):
    #Code Here
    for i in range (5) :
        for j in range (5) :
            if lst[i][j] == '-' :
                lst[i][j] = '0'
            #check front
            if(lst[i][j]!= '#') : 
                if j<4 and (lst[i][j+1] == '#' ) :
                    lst[i][j]  = str(int(lst[i][j]) + 1)
                #check back
                if j>0 and lst[i][j-1] == '#' :
                    lst[i][j]  = str(int(lst[i][j]) + 1)

                #check top
                if i>0 and lst[i-1][j] == '#'  :
                    lst[i][j]  = str(int(lst[i][j]) + 1)
                #check buttom
                if i<4 and lst[i+1][j] == '#'  :
                    lst[i][j]  = str(int(lst[i][j]) + 1)

                #check left top coener
                if i>0 and j>0 and lst[i-1][j-1] == '#':
                    lst[i][j]  = str(int(lst[i][j]) + 1)

                #check left down corner
                if i<4 and j>0 and lst[i+1][j-1] == '#' :
                    lst[i][j]  = str(int(lst[i][j]) + 1)
                #check right top coener
                if i>0 and j<4 and lst[i-1][j+1] == '#' :
                    lst[i][j]  = str(int(lst[i][j]) + 1)
                #check right bottom corner
                if i<4 and j<4 and lst[i+1][j+1] == '#' :
                    lst[i][j]  = str(int(lst[i][j]) + 1)

    return lst

print("*** Minesweeper ***")

lst_input = []

input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")