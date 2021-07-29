def push(stack,item):
    stack.append(item)
    
def isempty(stack):
    return len(stack)==0
    
def printl(stack):
    for i in range(0,len(stack)):
        print(stack[i])
        
def reverse(stack):
    if(not isempty(stack)):
        a=stack.pop()
        reverse(stack)
        insert(stack,a)

def insert(stack,item):
    if (isempty(stack)):
        push(stack,item)
    else:
        a=stack.pop()
        insert(stack,item)
        push(stack,a)
    
    
stack=[]
push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)
push(stack,5)
printl(stack)
print()
reverse(stack)
printl(stack)
