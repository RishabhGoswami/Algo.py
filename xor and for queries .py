def xor(m,n):
    count=0
    while(m!=n):
        m=m>>1
        n=n>>1
        count+=1
    return m>>count
    
def ands(n,m):
    count=0
    while(n==m):
        n=n<<1
        m=m<<1
        count+=1
    return m>>count
    
print(ands(16,20))
