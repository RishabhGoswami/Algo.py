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
    def countl(self):
        temp=self.head
        c=0
        while(temp):
            c=c+1
            temp=temp.next
        return c
        
    def reverse(self):
        prev=None
        curr=self.head
        while(curr):
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        self.head=prev
        
    def printl(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        
def add(l1):
    l1.reverse()
    temp=l1.head
    carry=0
    b=1
    while(temp):
        a=temp.data
        if(a+b+carry<=9):
            temp.data=(a+b+carry)
            carry=0
            break
        else:
            if(a+b+carry==10):
                carry=1
                number=0
            else:
                number=(a+b+carry)-10
                carry=1
            temp.data=(number)
        b=0
        temp=temp.next
    l1.reverse()
    if(carry==1):
        l1.push(1)
            
if __name__=='__main__':
    l1=Linke()
    l1.push(9)
    l1.push(9)
    l1.push(9)
    l1.push(1)

    add(l1)
    l1.printl()

    
