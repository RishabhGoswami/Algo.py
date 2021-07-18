def multiply(a,n):
    b=1
    for i in range(1,n+1):
        b=b*a
    return b
    
def nthroot(n,m):
    low=1
    high=m
    eps=10**(-6)
    while((high-low)>eps):
        mid=(low+high)/2
        if(multiply(mid,n)>m):
            high=mid
        else:
            low=mid
    return low
    
n=3
m=15
print(nthroot(n,m))
