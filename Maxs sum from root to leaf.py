class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def msum(root,s,maxs):
    if(root is None):
        return 
    if(root.left==None and root.right==None and s+root.data>maxs[0]):
        maxs[0]=s+root.data
        return 
    msum(root.left,s+root.data,maxs)
    msum(root.right,s+root.data,maxs)
    return maxs
    
def m(root):
    if(root.left ==None and root.left==None):
        return None
    else:
        s=0
        maxs=[0]
        a= msum(root,s,maxs)
        return a[0]
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(m(root))
