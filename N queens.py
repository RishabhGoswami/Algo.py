global n
n=4
def printl(board):
    for i in range(0,len(board)):
        print(*board[i])

def issafe(board,row,col):
    
    a=row
    b=col
    for i in range(col):
        if(board[row][i]==1):
            return False
           
    row=a
    col=b
    while(row>=0 and col>=0):
        if(board[row][col]==1):
            return False
        row-=1
        col-=1
        
    row=a
    col=b
    while(row<n and col>=0):
        if(board[row][col]==1):
            return False
        row+=1
        col-=1
        
    return True

def solvenq(board,col):
    if(col==4):
        return True
    for i in range(0,4):
        if(issafe(board,i,col)):
            board[i][col]=1
            if(solvenq(board,col+1)):
                return True
            board[i][col]=0
    return False

def solveq():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]
              
    if(solvenq(board,0) is False):
        print('no')
        return False
        
    printl(board)
    return True
    
solveq()
