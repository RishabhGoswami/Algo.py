def joseph(n,k):
    if(n==1):
        return 0
    a=joseph(n-1,k)
    b=(a+k)%n
    return b
    
print(joseph(7,3))
    
