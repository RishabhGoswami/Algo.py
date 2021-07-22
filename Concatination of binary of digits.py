import math
def con(n):
    s=1
    
    for i in range(2,n+1):
        d=int(math.log(i,2))+1
        s=(s*((2**d)))+i
    return (s)
    
print(con(4))
