def sliding(arr,k):
    l=[]
    ans=[]
    
    for i in range(0,len(arr)):
        if(len(l)>0 and l[0]==(i-k)):
            l.pop(0)
        while(len(l)>0 and arr[l[-1]]<arr[i]):
            l.pop()
        l.append(i)
        if(i>=(k-1)):
            ans.append(arr[l[0]])
    return ans
    
arr=[1,3,-1,-3,5,3,6,7]
k=3
print(sliding(arr,k))
        
        
