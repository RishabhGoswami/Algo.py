def infix_to_postfix(expression): #input expression
    OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators

    PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = [] # initially stack empty

    output = '' # initially output empty
    for ch in expression:

        if ch not in OPERATORS:  
            output+= ch

        elif ch=='(':
            stack.append('(')

        elif ch==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:

        output+=stack.pop()

    return output
    
expression='(A+(C+D*F+T*A)*B/C)'    
print('postfix expression: ',infix_to_postfix(expression))    
