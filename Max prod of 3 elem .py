def productof2(arr):
    max1=arr[0]
    max2=-10**9
    max3=-10**9
    
    min1=arr[0]
    min2=10**9
    for i in range(1,len(arr)):
        if(arr[i]>max1):
            max3=max2
            max2=max1
            max1=arr[i]
        elif(arr[i]>max2):
            max3=max2
            max2=arr[i]
        else:
            max3=arr[i]
            
        if(arr[i]<min1):
            min2=min1
            min1=arr[i]
        elif(arr[i]<min2):
            min2=arr[i]
    return(max(max1*max2*max3,max1*min1*min2))
            
arr=[-4, 1, -8, 9, 6]
print(productof2(arr))
