class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printdown(root,k):
    if(root):
        if(k==0):
            print(root.data)
        printdown(root.left,k-1)
        printdown(root.right,k-1)

def down(root,target,k):
    if(root is None):
        return -1
        
    if(root==target):
        printdown(root,k)
        return 0
        
    d1=down(root.left,target,k)
    if(d1!=-1):
        if(1+d1==k):
            print(root.data)
        else:
            printdown(root.right,k-d1-2)
        return 1+d1
        
    d2=down(root.right,target,k)
    if(d2!=-1):
        if(1+d2==k):
            print(root.data)
        else:
            printdown(root.left,k-d2-2)
        return 1+d2
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
    target = root.left.right
    down(root,target,2)

    
    
    
    
    
    
    
    
    
