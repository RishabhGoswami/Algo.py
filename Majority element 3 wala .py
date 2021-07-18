import math
def majority(arr):
    c1=0
    c2=0
    elem1=0
    elem2=0
    h=len(arr)
    
    for i in range(0,len(arr)):
        if(arr[i]==elem1):
            c1+=1
        elif(arr[i]==elem2):
            c2+=1
        elif(c1==0):
            c1=1
            elem1=arr[1]
        elif(c2==0):
            c2=1
            elem2=arr[i]
        else:
            c1-=1
            c2-=1
    e=0
    f=0
    for i in range(0,len(arr)):
        if(arr[i]==elem1):
            e=e+1
        elif(arr[i]==elem2):
            f=f+1
            
    d=math.floor(h/3)
    if(e>d):
        return elem1 
    elif(f>d):
        return elem2
    else:
        return -1

arr=[7,7,5,7,5,1,5,7,5,5,7,7,5]
print(majority(arr))
