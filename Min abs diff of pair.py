def binary(arr,x):
    low=0
    high=len(arr)
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]<x):
            low=mid+1
        elif(arr[mid]>x):
            high=mid-1
        else:
            return mid
    return -1
    
def pairs(arr,x):
    arr=sorted(arr)
    for i in range(0,len(arr)):
        if(binary(arr,arr[i]-x)>=0):
            return True
    return False
    
    
def minabs(arr,mins):
    arr=sorted(arr)
    low=0
    high=len(arr)-1
    i=-1
    j=-1
    while(low<high):
        if((arr[low]+arr[high])<mins):
            mins=(arr[low]+arr[high])
            i=low
            j=high
        if(arr[low]+arr[high]<0):
            low=low+1
        else:
            high=high-1
    print(arr[i],arr[j])
arr=[-6, -5, -3, 0, 2, 4, 9]
mins=10**9
(minabs(arr,mins))















