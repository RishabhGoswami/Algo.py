class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def first(inn,post,lenn):
    global mp,index
    for i in range(0,len(inn)):
        mp[inn[i]]=i
    index=0
    return second(inn,post,0,lenn-1)

def second(inn,post,istart,iend):
    
    global index,mp
    
    if(istart>iend):
        return None
        
    a=post[index]
    node=Node(a)
    index+=1
    if(istart==iend):
        return node
    iindex=mp[a]
    
    node.left=second(inn,post,istart,iindex-1)
    node.right=second(inn,post,iindex+1,iend)
    
    return node
    
def preorder(root):
    if(root):
        preorder(root.left)
        print(root.data)
        preorder(root.right)
        
if __name__=='__main__':
    inn =  ['D', 'B', 'E', 'A', 'F', 'C' ]
    post=[ 'A', 'B', 'D', 'E', 'C', 'F' ]
    mp={}
    index=0
    lenn=len(inn)
    a=first(inn,post,lenn)
    preorder(a)
