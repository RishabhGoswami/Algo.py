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

    def leng(self):
        slow=self.head
        fast=self.head
        while(slow and slow.next and fast and fast.next and fast.next.next):
            if(slow.data==fast.data ):
                break
            slow=slow.next
            fast=fast.next.next
            
        if(slow.data!=fast.data):
            return 0
        else:
            slow=self.head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            return slow.data
if __name__=='__main__':
    l=Linke()
    l.push(4)
    l.push(5)
    l.push(2)
    l.push(1)
    l.head.next.next.next.next=l.head
    print(l.leng())
