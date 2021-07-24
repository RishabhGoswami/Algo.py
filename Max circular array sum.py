def circular(arr):
    for i in range(0,len(arr)):
        arr[i]=-1*arr[i]
    maxs=-10**9
    maxe=0
    e=0
    for i in range(0,len(arr)):
        e=e+arr[i]
        maxe=maxe+arr[i]
        if(maxs<maxe):
            maxs=maxe
        if(maxe<0):
            maxe=0
    a=(-e)-(-maxs)
    return a
    
arr=[5,-3,-2,6,-1,4]
print(circular(arr))
        
