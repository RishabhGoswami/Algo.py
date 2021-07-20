def next(arr):
    if(len(arr)==1):
        return arr
    lasti=-1
    for i in range(1,len(arr)):
        if(arr[i]>arr[i-1]):
            lasti=i
    if(lasti==-1):
        arr=sorted(arr)
        return arr
    index=lasti
    for i in range(lasti,len(arr)):
        if(arr[i]>arr[lasti-1] and arr[i]<arr[lasti] ):
            index=i
    arr[index],arr[lasti-1]=arr[lasti-1],arr[index]
    d=arr[lasti:]
    arr=(arr[0:lasti]+sorted(d))
    return (arr)
    
arr=[1,2,3,5,4,2]
print(next(arr))
