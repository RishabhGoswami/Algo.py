class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def conversion(arr):
    if (len(arr)>0):
        mid=len(arr)//2
        root=Node(arr[mid])
        root.left=conversion(arr[:mid])
        root.right=conversion(arr[mid+1:])
        return root
        
def inorder(c):
    if(c):
        print(c.data)
        inorder(c.left)
        inorder(c.right)
        
if __name__=='__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    c=conversion(arr)
    inorder(c)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
