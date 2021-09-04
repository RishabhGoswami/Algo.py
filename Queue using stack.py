class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def enqueue(self,data):
        self.s1.append(data)
        
    def dequeue(self):
        if(len(self.s1)==0 and len(self.s2)==0):
            print('both empty')
            return 
        elif(len(self.s1)>0 and len(self.s2)==0):
            while(len(self.s1)>0):
                a=self.s1.pop()
                self.s2.append(a)
            return self.s2.pop()
        else:
            return self.s2.pop()

if __name__=='__main__':
    q=Queue()
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    
    print(q.dequeue())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
