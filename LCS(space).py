def lcs(s1,s2,n,m):
  
    t=[[0 for j in range(m+1)] for i in range(2)]
    bi=bool
    
    for i in range(n+1):
        bi=i&1
        for j in range(m+1):
            if(i==0 or j==0):
                t[bi][j]=0
            elif(s1[i-1]==s2[j-1]):
                t[bi][j]=t[1-bi][j-1]+1
            else:
                t[bi][j]=max(t[1-bi][j],t[bi][j-1])
    return t[bi][m]
    
s1='acbxtyb'
s2='jdfcbxtn'
n=len(s1)
m=len(s2)
print(lcs(s1,s2,n,m))
