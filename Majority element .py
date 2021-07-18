def majority(arr):
    element=0
    count=0
    
    for i in  range(0,len(arr)):
        if(count==0):
            element=arr[i]
        if(arr[i]==element):
            count+=1
        else:
            count-=1
    return element
    
arr=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majority(arr))
