class Node:

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
    	 	
def morris_traversal(root):
	current = root
	while current is not None:
		if current.left is None:
			print( current.data)
			current = current.right
		else:
			pre = current.left
			while pre.right is not None and pre.right is not current:
				pre = pre.right
			if pre.right is None:
				pre.right = current
				current = current.left
			else:
				pre.right = None
				print( current.data)
				current = current.right
root = Node(1)
root.right=Node(3)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)

morris_traversal(root)

