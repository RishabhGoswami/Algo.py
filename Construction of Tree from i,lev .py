class Node:

	# A constructor for making a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def first(inn,level):
    global mp , preindex
    mp={}
    for i in range(0,len(level)):
        mp[level[i]]=i
    lenn=len(inn)
    return second(inn,0,lenn-1)
    
def second(inn,istart,iend):
    global mp ,inndex
    if(istart>iend):
        return None
    index=istart
    for i in range(istart+1,iend+1):
        if(mp[inn[i]]<mp[inn[index]]):
            index=i
    t=Node(inn[index])
            
    t.left=second(inn,istart,index-1)
    t.right=second(inn,index+1,iend)
    return t
    
def inorder(a):
    if(a):
        inorder(a.left)
        print(a.data)
        inorder(a.right)
# Root node of the trhee

inn = [4, 2, 5, 1, 6, 3, 7]
level = [1, 2, 3, 4, 5, 6, 7]

a=first(inn,level)
inorder(a)class Node:

	# A constructor for making a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def first(inn,level):
    global mp , preindex
    mp={}
    for i in range(0,len(level)):
        mp[level[i]]=i
    lenn=len(inn)
    return second(inn,0,lenn-1)
    
def second(inn,istart,iend):
    global mp ,inndex
    if(istart>iend):
        return None
    index=istart
    for i in range(istart+1,iend+1):
        if(mp[inn[i]]<mp[inn[index]]):
            index=i
    t=Node(inn[index])
            
    t.left=second(inn,istart,index-1)
    t.right=second(inn,index+1,iend)
    return t
    
def inorder(a):
    if(a):
        inorder(a.left)
        print(a.data)
        inorder(a.right)
# Root node of the trhee

inn = [4, 2, 5, 1, 6, 3, 7]
level = [1, 2, 3, 4, 5, 6, 7]

a=first(inn,level)
inorder(a)
