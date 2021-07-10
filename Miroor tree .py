class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.nextRight=None
        self.data=data
    
def mirror(root):
    
    if( nor root):
        return None
    l=[]
    l.append(root)
    while(len(l)>0):
        a=l[0]
        l.pop(0)
        a.left,a.right=a.right,a.left
        if(a.left):
            l.append(a.left)
        if(a.right):
            l.append(a.right)
        
def inorder(root):
    if(root):
        print(root.data)
        inorder(root.left)
        inorder(root.right)
        
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    print(inorder(root))
    mirror(root)
    print(inorder(root))
    
