arr = [[6,4], [3,6], [7,3]]
c=0
d=0
start=0
for i in range(0,len(arr)):
    c=c+(arr[i][0]-arr[i][1])
    if(c<0):
        start=i+1
        d=d+c
        c=0
if(c+d>=0):
    print( start)
else:
    print( -1)
    
    
