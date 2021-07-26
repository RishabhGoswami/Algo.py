class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linke:
    def __init__(self):
        self.head=None
        
    def push(self,data):
        newp=Node(data)
        newp.next=self.head
        self.head=newp
            
    def printl(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def reverse(self):
        curr=self.head
        nex=None
        while(curr.next):
            nex=curr.next
            curr.next=nex.next
            nex.next=self.head
            self.head=nex
        
        
if __name__=='__main__':
    l=Linke()
    l.push(4)
    l.push(5)
    l.push(2)
    l.push(1)
    l.printl()
    print( )
    l.reverse()
    l.printl()
    
    
    
    
    
    
    
    
    
    
