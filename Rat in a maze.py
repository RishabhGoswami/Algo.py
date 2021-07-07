def issafe(maze,x,y):
    if(x>=0 and x<4 and y>=0 and y<4 and maze[x][y]==1):
        return True
    return False
    
def printl(sol):
    for i in range(0,len(sol)):
        print(*sol[i])
        
def solvemaze( maze ):
     
    # Creating a 4 * 4 2-D list
    sol = [ [ 0 for j in range(4) ] for i in range(4) ]
     
    if solvemazeu(maze, 0, 0, sol) == False:
        print("Solution doesn't exist");
        return False
     
    printl(sol)
    return True
    
def solvemazeu(maze,x,y,sol):
    if(x==3 and y==3 and maze[x][y]==1):
        sol[x][y]=1
        return True
    if(issafe(maze,x,y)):
        if(sol[x][y]==1):
            return False
        sol[x][y]=1
        if(solvemazeu(maze,x+1,y,sol)):
            return True
        if(solvemazeu(maze,x,y+1,sol)):
            return True
        if(solvemazeu(maze,x-1,y,sol)):
            return True
        if(solvemazeu(maze,x,y-1,sol)):
            return True
        sol[x][y]=0
        return False

if __name__ == "__main__":
    maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]
    solvemaze(maze)
