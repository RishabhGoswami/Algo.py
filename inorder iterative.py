class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inorder(root):
    s=[]
    curr=root
    while(True):
        if(curr):
            s.append(curr)
            curr=curr.left
        elif(s):
            curr=s.pop()
            print(curr.data)
            curr=curr.right
        else:
            break
    
        
    
    
if __name__=='__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    inorder(root)
    
    
    
    
    
    
    
    
    
    
    
