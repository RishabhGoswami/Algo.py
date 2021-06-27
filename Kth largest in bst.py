class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def klarge(root,k,c):
    if(root is None or c[0]>=k):
        return None
    klarge(root.right,k,c)
    c[0]+=1
    if(c[0]==k):
        print(root.data)
    klarge(root.left,k,c)

    
def k(root):
    c=[0]
    return klarge(root,3,c)

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
k(root)
