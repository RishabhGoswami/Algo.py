class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def minv(root):
    while(root.left):
        root=root.left
    return root
    
def dele(root,key):
    if(root is None):
        return root
    if(root.data<key):
        root.right=dele(root.right,key)
    elif(root.data>key):
        root.left=dele(root.left,key)
    else:
        if(root.left is None):
            temp=root.right
            root=None
            return temp
        elif(roor.right is None):
            temp=root.left
            root=None
            return temp
        else:
            temp=minv(root.right)
            root.data=temp.data
            root.right=dele(root.right,temp.data)
    return root
        
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)
        
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(13)
# inorder(root)
# print( )
a=dele(root,6)
inorder(a)
