def nextsmall(s):
    d=len(s)
    if(d%2==0):
        center=''
    else:
        center=s[d//2]
    left=s[0:d//2]
    right=left[::-1]
    pal=left+center+right
    if(pal>s):
        print(pal)
    else:
        if(center):
            if(center<'9'):
                center=str(int(center)+1)
                print(left+center+right)
                return
            else:
                center='0'
        if('9'*(d)==s):
            print('1'+'0'*(d-1)+'1')
        else:
            left=inc(left)
            print(left+center+left[::-1])


def inc(left):
    leftl=list(left)
    last=len(left)-1
    while(leftl[last]=='9'):
        leftl[last]='0'
        last-=1
    leftl[last]=str(int(leftl[last])+1)
    return ''.join(leftl)
    
s='91'
nextsmall(s)
