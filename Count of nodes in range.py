# Python3 program to count BST nodes
# withing a given range

# Utility function to create new node
class newNode:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Returns count of nodes in BST in
# range [low, high]
def getCount(root, low, high):
	
	# Base case
	if root == None:
		return 0
		
	# Special Optional case for improving
	# efficiency
	if root.data == high and root.data == low:
		return 1

	# If current node is in range, then
	# include it in count and recur for
	# left and right children of it
	if root.data <= high and root.data >= low:
		return (1 + getCount(root.left, low, high) +
					getCount(root.right, low, high))

	# If current node is smaller than low,
	# then recur for right child
	elif root.data < low:
		return getCount(root.right, low, high)

	# Else recur for left child
	else:
		return getCount(root.left, low, high)

# Driver Code
if __name__ == '__main__':
	
	# Let us construct the BST shown in
	# the above figure
	root = newNode(10)
	root.left = newNode(5)
	root.right = newNode(50)
	root.left.left = newNode(1)
	root.right.left = newNode(40)
	root.right.right = newNode(100)
	
	# Let us constructed BST shown in above example
	#	 10
	#	 / \
	# 5	 50
	# /	 / \
	# 1	 40 100
	l = 5
	h = 45
	print("Count of nodes between [", l, ", ", h,"] is ",
									getCount(root, l, h))

# This code is contributed by PranchalK
