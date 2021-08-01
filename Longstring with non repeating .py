def longest(arr):
    s=dict()
    left=0
    right=0
    n=len(arr)
    maxl=-1
    while(right<n):
        if(arr[right] in s):
            left=max(left,s[arr[right]]+1)
        s[arr[right]]=right
        maxl=max(maxl,(right-left)+1)
        right+=1
    return maxl
            
    
arr='abcaabcdba'
print(longest(arr))
