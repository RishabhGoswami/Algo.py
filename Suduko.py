def issafe(grid,val,row,col):
    for k in range(0,9):
        if(grid[k][col]==val):
            return False
        if(grid[row][k]==val):
            return False
        if(grid[3 * (row // 3) + k // 3][3 * (col // 3) + k % 3] == val):
            return False
    return True

def solve(grid):
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if(grid[i][j]==0):
                for k in range(1,10):
                    if(issafe(grid,k,i,j)):
                        grid[i][j]=k
                        if(solve(grid)):
                            return True
                        else:
                            grid[i][j]=0
                return False
    return True
           
def printl(grid):
    for i in range(0,len(grid)):
        print(*grid[i])
    
    
if __name__=="__main__":
     
    # creating a 2D array for the grid
    grid =[[0 for x in range(9)]for y in range(9)]
     
    # assigning values to the grid
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
     
    # if success print the grid
    if(solve(grid)):
        printl(grid)
    else:
        print ("No solution exists")
