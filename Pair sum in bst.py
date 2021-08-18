class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def pair(root,target):
    s1=[]
    s2=[]
    temp=root
    while(temp):
        s1.append(temp)
        temp=temp.left
    temp=root
    while(temp):
        s2.append(temp)
        temp=temp.right

    while(s1[-1].data<s2[-1].data and len(s1)>0 and len(s2)>0):
        a=s1[-1]
        b=s2[-1]
        c=a.data+b.data
        if(c==target):
            print(a.data,b.data)
            return 
        elif(c<target):
            if(a.right):
                s1.pop()
                d=a.right
                s1.append(d)
                while(d.left):
                    s1.append(d.left)
                    d=d.left
            else:
                s1.pop()
        else:
            if(a.left):
                s2.pop()
                d=a.left
                s2.append(d)
                while(d.right):
                    s2.append(d.right)
                    d=d.right
            else:
                s2.pop()
    return -1
    
if __name__=='__main__':
    root=Node(70)
    root.left=Node(50)
    root.right=Node(80)
    root.left.left=Node(40)
    root.left.right=Node(60)
    root.left.left.left=Node(30)
    root.left.right.left=Node(55)
    root.right.right=Node(90)
    print(pair(root,170))
