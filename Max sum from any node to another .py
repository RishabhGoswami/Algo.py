class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def maxs(root):
    if(root is None):
        return 0
    l=maxs(root.left)
    r=maxs(root.right)
    m1=max(max(l,r)+root.data,root.data)
    m2=max(m1,(l+r+root.data))
    maxs.res=max(maxs.res,m2)
    return m1
    
def m(root):
    maxs.res=-1
    maxs(root)
    return maxs.res
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print (m(root))
