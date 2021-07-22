def diagonal(mat,n,m):
    arr=[[] for _ in range(n+m-1)]
    for i in range(m):
        for j in range(n):
            arr[i+j].append(mat[j][i])
    
    for i in range(len(arr)):
        for j in range(len(arr[i])-1,-1,-1):
            print(arr[i][j],end=' ')
        print( )
        
mat=[[1, 2, 3, 4],[ 5, 6, 7, 8],[9, 10, 11, 12 ],[13, 14, 15, 16 ],[ 17, 18, 19, 20]]
n=5
m=4
diagonal(mat,n,m)
        
