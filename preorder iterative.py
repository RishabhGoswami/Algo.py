class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inorder(root):
    s=[]
    while(len(s)>0):
        a=s.pop()
        print(a.data)
        if(a.right):
            s.append(a.right)
        if(a.left):
            s.append(a.left)
            
    
        
    
    
if __name__=='__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    inorder(root)
    
    
    
    
    
    
    
    
    
    
    
