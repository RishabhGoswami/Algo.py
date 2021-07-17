def two(arr):
    low=0
    high=len(arr)-2
    
    while(low<=high):
        mid=(low+high)>>1
        if(arr[mid]==arr[mid^1]):
            low=mid+1
        else:
            high=mid-1
    return arr[low]
    
arr=[1,1,2,2,3,3,4]
print(two(arr))
