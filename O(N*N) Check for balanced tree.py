class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def height(root):
    if(root is None):
        return 0
    else:
        return (1+max(height(root.left),height(root.right)))
        
def isbal(root):
    
    if root is None:
        
        return True
    
    lefth=height(root.left)
    
    righth=height(root.right)
    
    if(abs(lefth-righth)<=1 and isbal(root.left)is True and isbal(root.right) is True):
        
        return True
        
    return False
        


root = Node(44)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(isbal(root))
