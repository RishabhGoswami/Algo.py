class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printl(root):
    arr=[]
    printlroot(root,arr)
    
def printlroot(root,arr):
    if(root):
        arr.append(root.data)
        if(root.left==None and root.right==None):
            print(arr)
        printlroot(root.left,arr)
        printlroot(root.right,arr)
        arr.pop()
    
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    printl(root)
    
    
    
    
    
    
    
    
    
    
    
