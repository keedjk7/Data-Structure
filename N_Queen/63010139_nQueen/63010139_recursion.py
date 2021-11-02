import time

def isSafe(board, row, colum):
 
    #check straight line 
    #print_Board(board,N)
    for i in range(N):
        if (board[row][i] == 'Q') or (board[i][colum] == 'Q'):
            return False
    #check diagonal
    for i in range(N):
        for j in range(N):
            if (i+j == row + colum ) or (i-j==row-colum):
                if (board[i][j] == 'Q'):
                    return False
    
    return True
 
 
def printSolution(board,N):
    for r in range(N):
        for c in range(N):
            print(board[r][c],end=" ")
        print()
    print()
 
 
def nQueen(board, N, r,solution):
 
    # if `N` queens are placed successfully, print the solution
    if r == N:
        printSolution(board,N)
        solution += 1
        return solution
 
    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(N):
 
        # if no two queens threaten each other
        if isSafe(board, r, i):
            # place queen on the current square
            board[r][i] = 'Q'
 
            # recur for the next row
            solution = nQueen(board, N, r + 1,solution)
 
            # backtrack and remove the queen from the current square
            board[r][i] = '–'
 
    return solution

if __name__ == '__main__':
    
    start_time = time.time()
    # `N × N` chessboard
    N = int(input("Enter N Queen : "))
 
    # `board[][]` keeps track of the position of queens in
    # the current configuration
    board = [['–']*N for i in range(N)]
    
    solution = 0

    solution = nQueen(board,N, 0,solution)

    print("Number of  Solution :",solution)
    print("Runtime :",time.time() - start_time,"seconds")