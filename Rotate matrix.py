def rotate(mat):
    for i in range(0,len(mat)-1):
        for j in range(i+1,len(mat)):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    i=0
    while(i<len(mat)):
        for j in range(0,len(mat)//2):
            mat[i][j],mat[i][len(mat)-1-j]=mat[i][len(mat)-1-j],mat[i][j]
        i=i+1
    return mat
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotate(mat))
