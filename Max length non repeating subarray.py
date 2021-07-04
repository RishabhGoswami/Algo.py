s='geeksforgeeks'
h={}
start=0
maxl=0

for i in range(0,len(s)):
    if(s[i] in h):
        start=max(start,(h[s[i]]+1))
    maxl=max(maxl,(i-start)+1)
    h[s[i]]=i
    
print(maxl)
