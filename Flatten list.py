class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.down=None

class Linke:
    def __init__(self):
        self.head=None
    def push(self,head,data):
        newp=Node(data)
        newp.down=head
        head=newp
        return head
    def printl(self,head):
        while(head):
            print(head.data)
            head=head.down
    def merge(self,a,b):
        if (a is None):
            return b
        if( b is None):
            return a
        if(a.data<=b.data):
            res=a
            res.down=self.merge(res.down,b)
        else:
            res=b
            res.down=self.merge(a,res.down)
        res.right=None
        return res
        
    def flatten(self,root):
        if (root is None or root.right is None):
            return root
        root.right=self.flatten(root.right)
        root=self.merge(root,root.right)
        return root
        
if __name__=='__main__':
    L = Linke()
    L.head = L.push(L.head, 30);
    L.head = L.push(L.head, 8);
    L.head = L.push(L.head, 7);
    L.head = L.push(L.head, 5);
      
    L.head.right = L.push(L.head.right, 20);
    L.head.right = L.push(L.head.right, 10);
      
    L.head.right.right = L.push(L.head.right.right, 50);
    L.head.right.right = L.push(L.head.right.right, 22);
    L.head.right.right = L.push(L.head.right.right, 19);
      
    L.head.right.right.right = L.push(L.head.right.right.right, 45);
    L.head.right.right.right = L.push(L.head.right.right.right, 40);
    L.head.right.right.right = L.push(L.head.right.right.right, 35);
    L.head.right.right.right = L.push(L.head.right.right.right, 20);
    L.head=L.flatten(L.head)
    L.printl(L.head)
