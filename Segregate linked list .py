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
            
    def seg(self):
        temp=self.head
        c=0
        end=self.head
        while(end.next):
            end=end.next
            c=c+1
        if(c%2!=0):
            c=c//2+1
        else:
            c=c//2
        temp=self.head
        while(c>0):
            end.next=temp.next
            temp.next=temp.next.next
            end.next.next=None
            temp=temp.next
            end=end.next
            c=c-1
        

if __name__=='__main__':
    l=Linke()
    l.push(3)
    l.push(5)
    l.push(4)
    l.push(1)
    (l.seg())
    l.printl()
