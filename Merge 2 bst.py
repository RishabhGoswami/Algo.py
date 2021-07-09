class newNode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)
        
def merge(root1,root2):
    s1=[]
    s2=[]
    c1=root1
    c2=root2
    if(not root1):
        return inorder(root2)
    if(not root1):
        return inorder(root1)
    while(c1 or s1 or c2 or s2):
        if(c1 or c2):
            if(c1):
                s1.append(c1)
                c1=c1.left
            if(c2):
                s2.append(c2)
                c2=c2.left
        else:
            if(not s1):
                while(s2):
                    c2=s2.pop()
                    c2.left=None
                    inorder(c2)
                    return
            if(not s2):
                while(s1):
                    c1=s1.pop()
                    c1.left=None
                    inorder(c1)
                    return
            c1=s1.pop()
            c2=s2.pop()
            if(c1.data<c2.data):
                print(c1.data)
                c1=c1.right
                s2.append(c2)
                c2=None
            else:
                print(c2.data)
                c2=c2.right
                s1.append(c1)
                c1=None

        
if __name__=='__main__':
    root1 = newNode(30)
    root1.left = newNode(1)
    root1.right = newNode(50)
    
    root2 = newNode(4)
    root2.left = newNode(2)
    root2.right = newNode(6)
    
    merge(root1,root2)
