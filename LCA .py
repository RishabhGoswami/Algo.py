class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
def lca(root,n1,n2):
    if(root is None):
        return None
    if(root.data==n1 or root.data==n2):
        return root.data
    left=lca(root.left,n1,n2)
    right=lca(root.right,n1,n2)
    if(left!= None and right!=None):
        return root.data
    if(left==None and right==None):
        return None
    return (left if left!=None else right)
        
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    print(lca(root,3,7))
    
