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















