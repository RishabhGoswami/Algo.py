class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.nextRight=None
        self.data=data
    
def zigzag(root):
    s1=[]
    s2=[]
    s1.append(root)
    
    while(len(s1)>0 or len(s2)>0):
        while(len(s1)>0):
            t=s1[-1]
            s1.pop(-1)
            print(t.data)
            if(t.right):
                s2.append(t.right)
            if(t.left):
                s2.append(t.left)
        while(len(s2)>0):
            t=s2[0]
            s2.pop(0)
            print(t.data)
            if(t.right):
                s1.append(t.right)
            if(t.left):
                s1.append(t.left)
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    zigzag(root)
    
