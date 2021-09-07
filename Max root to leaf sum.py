class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def rootpathsum(root,c,mins):
    if(root is None):
        return 0
    
    else:
        c=c+root.data
        if(root.left is None and  root.right is None):
            if(c>mins[0]):
                mins[0]=c
        else:
            rootpathsum(root.left,c,mins)
            rootpathsum(root.right,c,mins)


def temp(root):
    c=0
    mins=[-1]
    (rootpathsum(root,c,mins))
    print(mins[0])

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    (temp(root))

    
    
    
    
    
    
    
    
    
    
    
    
