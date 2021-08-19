class newNode:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def diag(root):
    m={}
    d=0
    a= diagonal(root,m,d)
    for i,j in a.items():
        print(j)
        
def diagonal(root,m,d):
    if(root):
        if(d not in m):
            m[d]=[root.data]
        else:
            m[d].append(root.data)
        diagonal(root.left,m,d+1)
        diagonal(root.right,m,d)
    return m
    
if __name__ == '__main__':
	
	# Let us construct the BST shown in
	# the above figure
	root = newNode(30)
	root.left = newNode(17)
	root.right = newNode(40)
	root.left.left = newNode(15)
	root.left.right = newNode(20)
	(diag(root))
