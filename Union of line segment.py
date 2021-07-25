def klees(segment):
    n=len(segment)
    points=[0 for i in range(2*n)]
    for i in range(0,n):
        points[i*2]=(segment[i][0],False)
        points[i*2+1]=(segment[i][1],True)
    points=sorted(points,key=lambda x:x[0])
    result=0
    count=0
    print(points)
    for i in range(0,2*n):
        if(i>0 and count>0 and points[i][0]>points[i-1][0]):
            result+=points[i][0]-points[i-1][0]
        if(points[i][1]):
            count-=1
        else:
            count+=1
    return result
    
segment=[(2, 5), (4, 8), (9, 12)]
print(klees(segment))
