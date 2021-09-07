class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def rootpathsum(root,l,mins):
    if(root is None):
        return 0
    
    else:
        l.append(root.data)
        if(root.left is None and  root.right is None):
            if(sum(l)>mins[0]):
                mins[0]=sum(l)
        else:
            rootpathsum(root.left,l,mins)
            rootpathsum(root.right,l,mins)
        l.pop()


def temp(root):
    l=[]
    mins=[-1]
    (rootpathsum(root,l,mins))
    print(mins[0])

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    (temp(root))

    
    
    
    
    
    
    
    
    
    
    
    
