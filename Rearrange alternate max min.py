def maxmin(arr):
    n=len(arr)
    maxd=n-1
    mind=0
    maxe=arr[n-1]+1
    
    for i in range(0,len(arr)):
        if(i%2==0):
            arr[i]=arr[i]+(arr[maxd]%maxe)*maxe
            maxd-=1
        else:
            arr[i]=arr[i]+(arr[mind]%maxe)*maxe
            mind+=1
    for i in range(0,n):
        arr[i]=arr[i]//maxe
        
    return arr
    
arr=[1,3,4,5,13]
print(maxmin(arr))
            
        
