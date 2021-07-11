def subsetsum(arr,cap,n):
    t=[[0 for j in range(cap+1)] for i in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,cap+1):
            if(i==0):
                t[i][j]=(10**9)-1
            if(j==0):
                t[i][j]=0
            if(i==1):
                if(arr[0]%i==0):
                    t[i][j]=j//arr[0]
                else:
                    t[i][j]=(10**9)-1
    t[0][0]=(10**9)-1
    t[1][0]=0
    # print(t[1])
    for i in range(1,n+1):
        for j in range(1,cap+1):
            if(arr[i-1]<=cap):
                t[i][j]=min(1+t[i][j-arr[i-1]] , t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    # for i in range(0,n):
    #     print(*t[i])
    # print(n,cap)
    return t[n][cap]
    
    
arr=[3,7,4]
cap=49
n=len(arr)
print(subsetsum(arr,cap,n))
