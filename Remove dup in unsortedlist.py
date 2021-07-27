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
    def dup(self):
        s=set()
        temp=self.head
        s.add(temp.data)
        while(temp.next):
            if(temp.next.data in s):
                temp.next=temp.next.next
            else:
                s.add(temp.next.data)
                temp=temp.next
if __name__=='__main__':
    l1=Linke()
    l1.push(9)
    l1.push(9)
    l1.push(8)
    l1.push(1)
    l1.push(8)
    l1.dup()

    l1.printl()

    
