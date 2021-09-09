class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def convert(root):
    prev=Node(-1)
    return final(root,prev)
    
def final(root,prev):
    if(root is None):
        return True
    left=final(root.left,prev)
    if(root.data<=prev.data):
        return False
    prev.data=root.data
    return left and final(root.right,prev)
    
    
def insert(root,data):
    if(root is  None):
        return Node(data)
    else:
        if(root.data==data):
            return root
        elif(root.data<data):
            root.right=insert(root.right,data)
        else:
            root.left=insert(root.left,data)
        return root
    

    
    

    
if __name__=='__main__':
    root=None
    keys = [ 20, 8, 22, 4, 12, 10, 14 ]
    k=4
    for i in keys:
        root=insert(root,i)
    # inorder(root)
    swap(root)
    print(convert(root))
