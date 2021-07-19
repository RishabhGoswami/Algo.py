def sliding(arr,dep):
    d=[]
    for i in range(0,len(arr)):
         d.append((dep[i],i))
    d.sort()
    print(d)
    end=d[0][0]
    ans=[1]
    for i in range(1,len(d)):
        if(arr[d[i][1]]>end):
            end=d[i][0]
            ans.append(d[i][1]+1)
    return ans
        
    
arr=[1,0,3,8,5,8]
dep=[2,6,4,9,7,9]
print(sliding(arr,dep))
        
        
