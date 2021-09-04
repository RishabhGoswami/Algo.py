class Minstack():
    def __init__(self,cmin):
        self.cmin=cmin
        self.s=[]
        
    def push(self,data):
        if(data>=self.cmin):
            self.s.append(data)
        else:
            a=(2*data)-self.cmin
            self.s.append(a)
            self.cmin=data
            
    def pop(self):
        a=self.s[-1]
        if(a>=self.cmin):
            self.s.pop()
        else:
            self.cmin=(2*self.cmin)-a
            self.s.pop()
    
    def getmin(self):
        return self.cmin
        
if __name__=='__main__':
    l=Minstack(10**9)
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.pop()
    print(l.getmin())
    
    
    
    
    
    
