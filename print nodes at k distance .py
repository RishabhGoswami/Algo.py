class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
      
def printk(root,k,level):
    if(root):
        if(level==k):
            print(root.data)
        printk(root.left,k,level+1)
        printk(root.right,k,level+1)

def printl(root,target,k):
    if (root is None):
        return -1
    if(root==target):
        printk(root,k,0)
        return 0
    
    l=printl(root.left,target,k)
    if(l!=-1):
        if(l+1==k):
            print(root.data)
        else:
            printk(root.right,k-l-2,0)
        return 1+l
    r=printl(root.right,target,k)
    
    if(r!=-1):
        if(r+1==k):
            print(root.data)
        else:
            printk(root.left,k-r-2,0)
        return 1+r
    return -1
        
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target=root.left.right
printl(root,target,2)
