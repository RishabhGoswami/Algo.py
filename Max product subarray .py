a=[-1,-3,10,0,60]
choice1=0
choice2=0
maxp=a[0]
minp=a[0]
ans=a[0]

for i in range(1,len(a)):
    choice1=a[i]*maxp
    choic2=a[i]*minp
    maxp=max(max(choice1,choice2),a[i])
    minp=min(min(choice1,choice2),a[i])
    ans=max(ans,maxp)
    
print(ans)
