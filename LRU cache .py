
class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class Cache:
    
    def __init__(self,cap):
        self.cap=cap
        self.dict=dict()
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def add(self,node):
        p=self.tail.prev
        p.next=node
        self.tail.prev=node
        node.next=self.tail
        node.prev=p
        
    def remove(self,node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p
        
    def get(self,key):
        if(key in self.dict):
            a=self.dict[key]
            self.remove(a)
            self.add(a)
            return a.val
        else:
            return -1
        
    def set(self,key,val):
        a=Node(key,val)
        self.add(a)
        self.dict[key]=a
        if(len(self.dict)>self.cap):
            p=self.head.next
            self.remove(p)
            del self.dict[p.key]
        

cache=Cache(3)
cache.set('a', 'apple')
cache.set('b', 'ball')
cache.set('c', 'cat')
cache.set('d', 'dog')
print(cache.get('a'))
print(cache.get('c'))
