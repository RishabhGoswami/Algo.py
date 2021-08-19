class newNode:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def merge(root1,root2):
    s1=[]
    s2=[]
    temp=root1
    while(temp):
        s1.append(temp)
        temp=temp.left
    temp=root2
    while(temp):
        s2.append(temp)
        temp=temp.left
    ans=[]
    while(len(s1)>0 and len(s2)>0):
        a=s1[-1]
        b=s2[-1]
        
        if(a.data==b.data):
            c=s1.pop()
            ans.append(c.data)
            if(a.right):
                t=a.right
                s1.append(t)
                while(t.left):
                    s1.append(t)
                    t=t.left
            c=s2.pop()
            if(b.right):
                t=b.right
                s2.append(t)
                while(t.left):
                    s2.append(t)
                    t=t.left
        elif(a.data<=b.data):
            c=s1.pop()
            ans.append(c.data)
            if(a.right):
                t=a.right
                s1.append(t)
                while(t.left):
                    s1.append(t)
                    t=t.left
        else:
            c=s2.pop()
            ans.append(c.data)
            if(b.right):
                t=b.right
                s2.append(t)
                while(t.left):
                    s2.append(t)
                    t=t.left
    print(ans)
    
if __name__ == '__main__':
	
	# Let us construct the BST shown in
	# the above figure
	root1 = newNode(30)
	root1.left = newNode(17)
	root1.right = newNode(40)
	root1.left.left = newNode(15)
	root1.left.right = newNode(20)
	
	root2 = newNode(24)
	root2.left = newNode(16)
	root2.right = newNode(29)
	root2.left.right = newNode(18)
	root2.right.right = newNode(30)
	
	merge(root1,root2)
