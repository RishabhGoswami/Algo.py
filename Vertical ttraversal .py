class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.nextRight=None
        self.data=data
    
def vertical(root):
    l=[]
    l.append(root)
    m={}
    hd={}
    hd[root]=0
    m[0]=[root.data]
    while(len(l)>0):
        a=l.pop(0)
        if(a.left):
            l.append(a.left)
            hd[a.left]=hd[a]-1
            c=hd[a.left]
            if(c not in m):
                m[c]=[]
            m[c].append(a.left.data)
        if(a.right):
            l.append(a.right)
            hd[a.right]=hd[a]+1
            c=hd[a.right]
            if(c not in m):
                m[c]=[]
            m[c].append(a.right.data)
    for i in m.items():
        print(*i)
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    vertical(root)
    
