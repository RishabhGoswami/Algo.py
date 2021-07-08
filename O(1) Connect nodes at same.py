class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.nextRight=None
        self.data=data
        
def getn(p):
    temp = p.nextRight
    while (temp != None):
        if (temp.left != None):
            return temp.left
        if (temp.right != None):
            return temp.right
        temp = temp.nextRight
    return None
    
def connect(p):
    if(not p):
        return 
    p.nextRight=None
    
    while(p!=None):
        q=p
        while(q!=None):
            if(q.left):
                if(q.right):
                    q.left.nextRight=q.right
                else:
                    q.left=getn(q)
            if(q.right):
                q.right.nextRight=getn(q)
            q=q.nextRight
        if(p.left):
            p=p.left
        elif(p.right):
            p=p.right
        else:
            p=getn(p)
# def connect(p):

# 	if (not p):
# 		return

# 	# Set nextRight for root
# 	p.nextRight = None

# 	# set nextRight of all levels one by one
# 	while (p != None):
# 		q = p

# 		# Connect all childrem nodes of p and
# 		# children nodes of all other nodes
# 		# at same level as p
# 		while (q != None):
# 			if (q.left):
# 				if (q.right):
# 					q.left.nextRight = q.right
# 				else:
# 					q.left.nextRight = getNextRight(q)

# 			if (q.right):
# 				q.right.nextRight = getNextRight(q)

# 			# Set nextRight for other nodes in
# 			# pre order fashion
# 			q = q.nextRight

# 		# start from the first node
# 		# of next level
# 		if (p.left):
# 			p = p.left
# 		elif (p.right):
# 			p = p.right
# 		else:
# 			p = getNextRight(p)
            
if __name__=='__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.right.right=Node(5)
    connect(root)
    print("Following are populated nextRight pointers in \n"
    "the tree (-1 is printed if there is no nextRight) \n")
    if(root.nextRight != None):
        print("nextRight of %d is %d \n" %(root.data,root.nextRight.data))
    else:
        print("nextRight of %d is %d \n" %(root.data,-1))
    if(root.left.nextRight != None):
        print("nextRight of %d is %d \n" %(root.left.data,root.left.nextRight.data))
    else:
        print("nextRight of %d is %d \n" %(root.left.data,-1))
    if(root.right.nextRight != None):
        print("nextRight of %d is %d \n" %(root.right.data,root.right.nextRight.data))
    else:
        print("nextRight of %d is %d \n" %(root.right.data,-1))
    if(root.left.left.nextRight != None):
        print("nextRight of %d is %d \n" %(root.left.left.data,root.left.left.nextRight.data))
    else:
        print("nextRight of %d is %d \n" %(root.left.left.data,-1))
    if(root.right.right.nextRight != None):
        print("nextRight of %d is %d \n" %(root.right.right.data,root.right.right.nextRight.data))
    else:
        print("nextRight of %d is %d \n" %(root.right.right.data,-1))
         
    print()
