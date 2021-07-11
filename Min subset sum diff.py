def subsetsum(arr,cap,n):
    t=[[True for j in range(cap+1)] for i in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,cap+1):
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
    
    a=t[n]
    mins=10**9
    for i in range(0,len(a)):
        if(a[i]==True):
            if(abs(cap-(2*i))<mins):
                mins=cap-(2*i)
        else:
            pass
    return mins
    
    
arr=[1,2,7,15]
cap=sum(arr)
n=len(arr)
print(subsetsum(arr,cap,n))
