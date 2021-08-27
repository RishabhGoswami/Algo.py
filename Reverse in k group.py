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
        
    def reverse(self,k):
        dummy=Node(0)
        dummy.next=self.head
        self.head=dummy
        curr=dummy
        prev=dummy
        nex=dummy
        count=0
        while(curr.next):
            count+=1
            curr=curr.next
        while(count>=k):
            curr=prev.next
            nex=curr.next
            for i in range(1,k):
                curr.next=nex.next
                nex.next=prev.next
                prev.next=nex
                nex=curr.next
            prev=curr
            count-=k
        return dummy.next
        
    def printl(self,a):
        temp=a
        while(temp):
            print(temp.data)
            temp=temp.next
        
if __name__=='__main__':
    l=Linke()
    l.push(8)
    l.push(7)
    l.push(6)
    l.push(5)
    l.push(4)
    l.push(3)
    l.push(2)
    l.push(1)
    a=l.reverse(2)
    l.printl(a)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
