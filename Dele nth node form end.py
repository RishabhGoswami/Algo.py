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
    
    def dele(self,n):
        fir=self.head
        sec=self.head
        for i in range(n):
            if(sec.next is None):
                if(i==(n-1)):
                    self.head=self.head.next
                return self.head
            sec=sec.next
        while(sec.next):
            sec=sec.next
            fir=fir.next
        fir.next=fir.next.next
        
    def printl(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

            
if __name__=="__main__":
    l1=Linke()
    l1.push(4)
    l1.push(2)
    l1.push(1)
    l1.dele(30)
    l1.printl()
    
    
    
    
    
    
    
    
    
    
    
