class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def diameter(root):
    ans=[-1]
    h=height(root,ans)
    return ans[0]
    
def height(root,ans):
    if(root is None):
        return 0
    lh=height(root.left,ans)
    rh=height(root.right,ans)
    ans[0]=max(ans[0],1+lh+rh)
    return 1+max(lh,rh)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(diameter(root))
    
    
    
    
    
    
    
    
    
    
    
    
    
