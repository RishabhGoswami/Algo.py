class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linke:
    def __init__(self):
        self.head=None
        
    def inserth(self,data):
        temp=self.head
        newp=Node(data)
        if(temp==None):
            self.head=newp
        else:
            self.head.prev=newp
            newp.next=self.head
            self.head= newp
    
    def insertt(self,data):
        newp=Node(data)
        temp=self.head
        if(temp==None):
            self.head=newp
            temp=self.head
        else:
            while(temp.next):
                temp=temp.next
            temp.next=newp
            newp.prev=temp

    def printl(self):
        node=self.head
        while(node):
            print(node.data)
            node=node.next
        
if __name__=='__main__':
    l=Linke()
    l.insertt(1)
    l.insertt(2)
    l.insertt(3)
    l.insertt(4)
    l.insertt(5)
    l.printl()
    
    
    
    
    
    
