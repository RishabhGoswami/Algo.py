def subsetsum(arr,cap,n):
    t=[[0 for j in range(cap+1)] for i in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,cap+1):
            if(i==0):
                t[i][j]=0
            if(j==0):
                t[i][j]=1
    t[0][0]=1
    for i in range(1,n+1):
        for j in range(1,cap+1):
            if(arr[i-1]<=cap):
                t[i][j]=t[i][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    
    return t[n][cap]
    
    
arr=[1,2,3]
cap=4
n=len(arr)
print(subsetsum(arr,cap,n))
