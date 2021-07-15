class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isp(root,r1):
    if(root is None):
        return False
    if(root.data==r1):
        return True
    return isp(root.left,r1) or isp(root.right,r1)
    
def flca(root,r1,r2):
    if(root is None):
        return None
    if(root.data==r1 or root.data==r2):
        return root
    left=flca(root.left,r1,r2)
    right=flca(root.right,r1,r2)
    if(left!=None and right!=None):
        return root
    if(left!=None):
        return left
    if(right !=None):
        return right
    return None
    
    
def findd(root,r1,level):
    if(root is None):
        return -1
    if(root.data==r1):
        return level
    left=findd(root.left,r1,level+1)
    if(left!=-1):
        return left
    return findd(root.right,r1,level+1)
    
def ans(root,r1,r2):
    lca=None
    if(isp(root,r1) and isp(root,r2)):
        lca=flca(root,r1,r2)
    else:
        return -1
    return findd(lca,r1,0) +findd(lca,r2,0)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.right.right = Node(8)
print(ans(root,7,4))










