def longest(s1,s2,n,m):
    
    t=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(s1[i-1]==s2[j-1]):
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i][j-1],t[i-1][j])
    
    a=t[n][m]
    print(a)
    
s1='agbcba'
s2=s1[::-1]
n=len(s1)
m=len(s2)
(longest(s1,s2,n,m))
