class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inorderp(root,k):
    if (root is None):
        return None
    n=None
    while(root):
        if(root.data>k):
            root=root.left
        elif(root.data<k):
            n=root.data
            root=root.right
        else:
            if(root.left):
                n=inleft(root)
            break
    if(root is None):
        return None
    return n

def inleft(root):
    if(root is None):
        return None
    a=root.left
    while(a.right):
        a=a.right
    return a.data

     
root = Node(8)
root.left = Node(4)
root.right = Node(12)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.left = Node(10)
root.right.right = Node(14)
print(inorderp(root,111))
