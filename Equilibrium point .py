def index(arr):
  
    right=0
    indices=[]
    total=sum(arr)
    for i in range(len(arr)-1,-1,-1):
        if(right==(total-(arr[i]+right))):
            indices.append(i)
        right+=arr[i]
    return indices
  
arr=[0, -3, 5, -4, -2, 3, 1, 0]
print(index(arr))
