class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class subtree:
    def __init__(self,min,max,size,isbst):
        self.min=min
        self.max=max
        self.size=size
        self.isbst=isbst
        
def largest(root):
    if(root is None):
        return subtree(10**9,-10**9,0,True)
    left=largest(root.left)
    right=largest(root.right)
    if(left.isbst and right.isbst and left.max<root.data<right.min):
        a=subtree(min(root.data,min(left.min,right.min)),max(root.data,max(left.max,right.max)),1+left.size+right.size,True)
    else:
        a=subtree(0,0,max(left.size,right.size),False)
        
    return a
        
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(15)
    root.right = Node(8)
    root.left.left = Node(12)
    root.left.right = Node(20)
    root.right.left = Node(5)
    root.right.right = Node(9)
    root.left.left.left = Node(2)
    root.left.left.right = Node(14)
    root.right.left.left = Node(4)
    root.right.left.right = Node(7)
    root.right.right.right = Node(10)
    print("The size of the largest BST is", largest(root).size)
        
        
        
        
        
        
        
        
        
        
        
