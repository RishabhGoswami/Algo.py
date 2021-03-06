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
def boundaryTraversal(root):
	# If there is only 1 node print it and return
	if root:
		if not root.left and not root.right:
			print (root.data)
			return

		# List to store order of traversed nodes
		list = []
		list.append(root)

		# Traverse left boundary without root
		# and last node
		temp = root.left
		while temp.left:
			list.append(temp)
			temp = temp.left

		# BFS designed to only include leaf nodes
		q = []
		q.append(root)
		while len(q) != 0:
			x = q.pop(0)
			if not x.left and not x.right:
				list.append(x)
			if x.left:
				q.append(x.left)
			if x.right:
				q.append(x.right)

		# Traverse right boundary without root
		# and last node
		list_r = []
		temp = root.right
		while temp.right:
			list.append(temp)
			temp = temp.right

		# Reversing the order
		list_r = list_r[::-1]

		# Concatenating the two lists
		list += list_r

		# Printing the node's data from the list
		print (" ".join([str(i.data) for i in list]))
	return

# Root node of the tree

root = Node(20)

root.left = Node(8)
root.right = Node(22)

root.left.left = Node(4)
root.left.right = Node(12)

root.right.left = Node(10)
root.right.right = Node(25)

boundaryTraversal(root)
