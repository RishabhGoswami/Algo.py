class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def serialize(root):
    if(root is None):
        return 'X'
    l=serialize(root.left)
    r=serialize(root.right)
    return str(root.data)+','+l+','+r

def de(root,s):
    arr=s.split(',')
    asss= defu(arr)
    return asss

def defu(arr):
    if(len(arr)==0):
        return None
    else:
        a=arr.pop(0)
        if(a=='X'):
            return None
        b=Node(a)
        b.left=defu(arr)
        b.right=defu(arr)
        return b
    

def inorder(root):
    if(root):
        print(root.data)
        inorder(root.left)
        inorder(root.right)
        
root = Node(8)
root.left = Node(4)
root.right = Node(12)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.left = Node(10)
root.right.right = Node(14)
a=(serialize(root))
s=(de(root,a))
inorder(s)
