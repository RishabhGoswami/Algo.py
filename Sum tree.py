# Python implementation of the approach
from collections import deque

# A binary tree node
class Node:

	# A constructor for making a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Function to print the nodes of a complete
# binary tree in boundary traversal order
def sumtree(root):
    if(root is None):
        return 0
    if(root.left is None and root.right is None):
        return root.data
    if(root.data==(sumtree(root.left)+sumtree(root.right))):
        return 2*root.data
    return -1

# Root node of the tree

root = Node(20)

root.left = Node(8)
root.right = Node(2)

root.left.left = Node(4)
root.left.right = Node(4)

root.right.left = Node(1)
root.right.right = Node(1)

print(sumtree(root))
