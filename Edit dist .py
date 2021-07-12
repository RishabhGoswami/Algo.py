def longests(s1,s2,n,m):
    t=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,m+1):
            if(i==0):
                t[i][j]=j
            if(j==0):
                t[i][j]=i
    t[0][0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(s1[i-1]==s2[j-1]):
                t[i][j]=t[i-1][j-1]
            else:
                t[i][j]=min(t[i-1][j]+1,t[i][j-1]+1,t[i-1][j-1]+1)
                
    a=t[n][m]
    return a
    
s1='sunday'
s2='saturday'
n=len(s1)
m=len(s2)
print(longests(s1,s2,n,m))
