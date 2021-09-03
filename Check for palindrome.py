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
    def reverse(self,a):
        prev=None
        curr=a
        while(curr):
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        a1=prev
        return a1
    def palindrome(self):
        b=self.head
        first=self.head
        second=self.head
        while(True):
            first=first.next.next
            if(first==None):
                a=second.next
                break
            if(first.next==None):
                a=second.next.next
                break
            second=second.next
        second.next=None
        a=self.reverse(a)
        flag=0
        while(b):
            if(a.data==b.data):
                pass
            else:
                flag=1
            a=a.next
            b=b.next
        if(flag==1):
            print('no')
            return 
        else:
            print('yes')
            return
if __name__=='__main__':
    l=Linke()
    l.push(10)
    l.push(200)
    l.push(20)
    l.push(10)
    # l.head.next.next.next.next.next=l.head.next.next
    (l.palindrome())
    
    
    
    
    
    
    
    
    
    
    
    
