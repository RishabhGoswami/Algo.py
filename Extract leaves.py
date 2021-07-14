class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class B2DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def convert(self,root):
        if(root is None):
            return 
        self.convert(root.left)
        if(root.left is None and root.right is None):
            if(self.head is None):
                self.head=root
            else:
                self.tail.right=root
                root.left=self.tail
            self.tail=root
        self.convert(root.right)
        return self.head
        
def printl(ass):
    while(ass):
        print(ass.data)
        ass=ass.right

def binary(root):
    a=B2DLL()
    return a.convert(root)
        
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
ass=binary(root)
printl(ass)
