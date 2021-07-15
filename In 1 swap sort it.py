def index(arr):
    prev=arr[0]
    x=-1
    y=-1
    
    for i in range(1,len(arr)):
        if(arr[i]<prev):
            if(x==-1):
                x=i-1
                y=i
            else:
                y=i
        prev=arr[i]
    arr[x],arr[y]=arr[y],arr[x]
    return arr
    
arr=[3, 5, 6, 9, 8, 7]
print(index(arr))
