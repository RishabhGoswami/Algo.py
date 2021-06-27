class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
        
def isbalance(root,isbal=True):
  
    if (root is None or not isbal):
        return 0,isbal
      
    lefth,isbal=isbalance(root.left,isbal)
    
    righth,isbal=isbalance(root.right,isbal)
    
    if(abs(lefth-righth)>1):
        isbal=False
        
    return 1+(max(lefth,righth)),isbal


root = Node(44)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
a=(isbalance(root,True))
print(a[1])
