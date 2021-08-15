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
        
def merge(l1,l2):
    if(l1 is None):
        return l2
    if(l2 is None):
        return l1
        
    if(l1.data<l2.data):
        return merges(l1,l2)
    return merges(l2,l1)
        
def merges(l1,l2):
    curr1=l1
    next1=l1.next
    curr2=l2
    next2=l2.next
    while (next1 != None and curr2 != None):
        if((curr2.data<=next1.data) and (curr2.data>=curr1.data)):
            next2 = curr2.next
            curr1.next=curr2
            curr2.next=next1
            curr1=curr2
            curr2=next2
        else:
            if(next1.next):
                next1=next1.next
                curr1=curr1.next
            else:
                next1.next=curr2
                return l1
    return l1
def printl(m):
    temp=m
    while(temp):
        print(temp.data)
        temp=temp.next
            
if __name__=="__main__":
    l1=Linke()
    l1.push(4)
    l1.push(2)
    l1.push(1)
    
    l2=Linke()
    l2.push(6)
    l2.push(5)
    l2.push(3)
    m=merge(l1.head,l2.head)
    printl(m)
    
    
    
    
    
    
    
    
    
    
    
