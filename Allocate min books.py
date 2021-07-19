def allo(arr,mid,stu):
    e=0
    c=1
    print(stu)
    for i in range(0,len(arr)):
        e=e+arr[i]
        if(e<=mid):
            pass
        else:
            e=arr[i]
            c=c+1
    if(c==stu):
        return True
    else:
        return False
        
def allocate(arr,n,stu):
    e=0
    maxs=10**9
    res=-1
    for i in range(0,len(arr)):
        e=e+arr[i]
        if(arr[i]<maxs):
            maxs=arr[i]
    low=maxs
    high=e
    while(low<=high):
        mid=(low+high)>>1
        if(allo(arr,mid,stu) is True):
            res=mid
            high=mid-1
        else:
            low=mid+1
    return res
    
arr=[12,34,67,90]
stu=2
n=len(arr)
print(allocate(arr,n,stu))
