from queue import Queue

class Stack:
    def __init__(self):
        self.q1=Queue()
        self.cur=0
        
    def push(self,data):
        self.cur+=1
        if(self.cur==1):
            self.q1.put(data)
        else:
            self.q1.put(data)
            ass=self.cur-1
            while(ass>0):
                a=self.q1.get()
                self.q1.put(a)
                ass-=1
                
        
    def top(self):
        if(self.q1.empty()):
            return None
        else:
            return self.q1.queue[0]
        
    def pop(self):
        if(self.q1.empty()):
            return None
        else:
            self.q1.get()
            self.cur-=1
    def size(self):
        if(self.q1.empty()):
            return None
        else:
            return self.cur
            
if __name__ == '__main__':
    s = Stack()
    s.push(1) 
    s.push(2) 
    s.push(3) 
  
    print("current size: ", s.size())
    print(s.top()) 
    s.pop() 
    print(s.top()) 
    s.pop() 
    print(s.top()) 
  
    print("current size: ", s.size())
    
    
    
    
    
    
