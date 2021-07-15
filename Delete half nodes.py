class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def convert(root):
    if(root is None):
        return None
    root.left=convert(root.left)
    root.right=convert(root.right)
#     Basically leaf nodes and nodes with single child are to be deleted
    if(root.left and root.right) or (root.left==None and root.right==None):
        return root
    if(root.left):
        return root.left
    if(root.right):
        return root.right
        
        
def inorder(root):
    if(root):
        print(root.data)
        inorder(root.left)
        inorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.right.right = Node(8)
inorder(root)
print( )
convert(root)
inorder(root)









