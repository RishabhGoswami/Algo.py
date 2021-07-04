s='geeksforgeeks'
h={}
st=0
maxl=0
start=0

for i in range(0,len(s)):
    if(s[i] not in h):
        h[s[i]]=i
    else:
        if(h[s[i]]>=st):
            curl=i-st
            if(curl>maxl):
                maxl=curl
                start=st
            st=h[s[i]]+1
        h[s[i]]=i
        
if(maxl<(i-st)):
    maxl=i-st
    start=st
    
print(s[start:start+maxl])
    
            
