class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def lca(root,n1,n2):
    if(root  is None):
        return None
    if(root.data==n1 or root.data==n2):
        return root
    left=lca(root.left,n1,n2)
    right=lca(root.right,n1,n2)
    if(left !=None and right!=None):
        return root
    if(left):
        return left
    else:
        return right
        
def findl(root,data,d,level):
    if(root):
        if(root.data==data):
            d.append(level)
            return
        findl(root.left,data,d,level+1)
        findl(root.right,data,d,level+1)
    
def dist(root,n1,n2):
    a=lca(root,n1,n2)
    d1=[]
    d2=[]
    if(lca):
        findl(a,n1,d1,0)
        findl(a,n2,d2,0)
        return d1[0]+d2[0]
    else:
        return -1

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    print(dist(root,3,4))
    
    
    
    
    
    
    
    
    
    
    
    
