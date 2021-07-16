class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def insert(root,data):
    if(root is None):
        return Node(data)
    if(root.data<data):
        root.right=insert(root.right,data)
    else:
        root.left=insert(root.left,data)
    return root
    
def isbst(root):
    if(checkbst(root,-10**9,10**9)):
        print('yes')
    else:
        print('no')

def checkbst(root,mini,maxi):
    if(root is None):
        return True
    if(root.data<mini or root.data>maxi):
        return False
    return checkbst(root.left,mini,root.data) and checkbst(root.right,root.data,maxi)

def swap(root):
    temp=root.left
    root.left=root.right
    root.right=temp
    
if __name__=='__main__':
    arr=[15, 10, 20, 8, 12, 16, 25]
    root=None
    for i in range(0,len(arr)):
        root=insert(root,arr[i])
    swap(root)
    isbst(root)
        























