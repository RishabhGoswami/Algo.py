def candy(arr):
    left=[1]
    right=[1 for _ in range(len(arr))]
    m=[]
    for i in range(1,len(arr)):
        if(arr[i]>arr[i-1]):
            left.append(left[i-1]+1)
        else:
            left.append(1)
    for i in range(len(arr)-2,-1,-1):
        if(arr[i]>arr[i+1]):
            right[i]=right[i+1]+1
    for i in range(0,len(left)):
        m.append(max(left[i],right[i]))
    return m
arr=[12,4,3,11,34,34,1,67]
print(candy(arr))
