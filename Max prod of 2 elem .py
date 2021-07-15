def productof2(arr):
    max1=arr[0]
    max2=-10**9
    
    min1=arr[0]
    min2=10**9
    for i in range(1,len(arr)):
        if(arr[i]>max1):
            max2=max1
            max1=arr[i]
        elif(arr[i]>max2):
            max2=arr[i]
            
        if(arr[i]<min1):
            min2=min1
            min1=arr[i]
        elif(arr[i]<min2):
            min2=arr[i]
    return(max(max1*max2,min1*min2))
            
arr=[-10, -3, 5, 6, -2]
print(productof2(arr))
