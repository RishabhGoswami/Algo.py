class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def ksmallest(root):
    global k
    if(root is None):
        return 0
    left=ksmallest(root.left)
    if(left):
        return left
    k=k-1
    if(k==0):
        return (root.data)
    return ksmallest(root.right)
    
def insert(node, data):
     
    # If the tree is empty, return a new node
    if node == None:
        return Node(data)
 
    # Otherwise, recur down the tree
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
 
    # return the (unchanged) node pointer
    return node
    
root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
k=2
print(ksmallest(root))
