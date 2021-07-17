def kele(arr1,arr2,n,m,k):
    
    if(n>m):
        return kele(arr2,arr1,m,n,k)
    
    while(low<=high):
        cut1=(low+high)>>1
        cut2=k-cut1
        if(cut1==0):
            l1=-10**9
        else:
            l1=arr1[cut1-1]
            
        if(cut1==n):
            r1=10**9
        else:
            r1=arr1[cut1]
            
        if(cut2==0):
            l2=-10**9
        else:
            l2=arr2[cut2-1]
            
        if(cut2==m):
            r2=10**9
        else:
            r2=arr2[cut2]
            
        if(l1<=r2 and l2<=r1):
            return max(l1,l2)
        elif(l1>r2):
            high=cut1-1
        else:
            low=cut1+1
            
    return 1
    
arr1=[1,3,4,7,10,12]
arr2=[2,3,6,15]
n=len(arr1)
m=len(arr2)
k=7
print(kele(arr1,arr2,n,m,k))
