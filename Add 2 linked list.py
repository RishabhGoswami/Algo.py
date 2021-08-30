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
        
def adds(l1,l2):
    dummy=Node(0)
    temp=dummy
    carry=0
    while(l1 or l2 or carry):
        sum=0
        if(l1 is not None):
            sum+=l1.data
            l1=l1.next
        if(l2 is not None):
            sum+=l2.data
            l2=l2.next
        sum+=carry
        carry=sum//10
        nod=Node(sum%10)
        temp.next=nod
        temp=temp.next
    return dummy.next
    
def printl(s):
    temp=s
    while(temp):
        print(temp.data)
        temp=temp.next
    
if __name__=='__main__':
    l1=Linke()
    l1.push(5)
    l1.push(4)
    l1.push(3)
    l1.push(2)
    l1.push(1)
    
    l2=Linke()
    l2.push(5)
    l2.push(4)
    l2.push(3)
    l2.push(2)
    l2.push(1)
    s=adds(l1.head,l2.head)
    printl(s)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
