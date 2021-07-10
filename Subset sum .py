def subsetsum(arr,cap,n):
    t=[[True for j in range(cap+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(cap+1):
            if(i==0):
                t[i][j]=False
            if(j==0):
                t[i][j]=True
    t[0][0]=True
            
    for i in range(1,n+1):
        for j in range(1,cap+1):
            if(arr[i-1]<=cap):
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][cap]
    def subsestsum(arr,k):
        for i in range(0,len(arr)):
            

arr=[2,30,7,8,10]
n=len(arr)
cap=11
print(subsetsum(arr,cap,n))
            
    




