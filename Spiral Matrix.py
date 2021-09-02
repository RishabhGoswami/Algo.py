def spiral(mat):
    top=0
    down=3
    left=0
    right=3
    dirs=0
    while(top<=down and left<=right):
        if(dirs==0):
            for i in range(left,right+1):
                print(mat[top][i])
            top=top+1
        elif(dirs==1):
            for i in range(top,down+1):
                print(mat[i][right])
            right=right-1
        elif(dirs==2):
            for i in range(right,left-1,-1):
                print(mat[down][i])
            down=down-1
        elif(dirs==3):
            for i in range(down,top-1,-1):
                print(mat[i][left])
            left=left+1
        dirs=(dirs+1)%4
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
(spiral(mat))
