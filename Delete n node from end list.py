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
    
    def countl(self):
        temp=self.head
        c=0
        while(temp):
            c=c+1
            temp=temp.next
        return c


    def dele(self,x):
        first=self.head
        second=self.head
        for i in range(x):
            if(second.next==None):
                if(i==(x-1)):
                    self.head=self.head.next
                return self.head
            second=second.next
        while(second.next):
            first=first.next
            second=second.next
        first.next=first.next.next
            
if __name__=='__main__':
    l=Linke()
    l.push(4)
    l.push(5)
    l.push(2)
    l.push(1)
    l.dele(1)
    l.printl()
