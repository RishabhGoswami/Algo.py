def merge(arr,n):
    temp=[0]*n
    return merges(arr,temp,0,n-1)

def merges(arr,temp,left,right):
    inv=0
    if(left<right):
        mid=(left+right)//2
        inv+=merges(arr,temp,left,mid)
        inv+=merges(arr,temp,mid+1,right)
        inv+=msort(arr,temp,left,mid,right)
    return inv

def msort(arr,temp,left,mid,right):
    i=left
    j=mid+1
    k=left
    inv=0
    
    while(i<=mid and j<=right):
        if(arr[i]<=arr[j]):
            temp[k]=arr[i]
            k=k+1
            i=i+1
        else:
            temp[k]=arr[j]
            inv+=(mid-i+1)
            k=k+1
            j=j+1
            
    while(i<=mid):
        temp[k]=arr[i]
        k=k+1
        i=i+1
    while(j<=right):
        temp[k]=arr[j]
        k=k+1
        j=j+1
    for i in range(left,right+1):
        arr[i]=temp[i]
    return inv
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = merge(arr, n)
print("Number of inversions are", result)
