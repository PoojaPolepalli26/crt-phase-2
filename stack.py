def push(stack,ele):
    stack.append(ele)
    print(ele,"inserted into the stack")
def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"deleted successfully")
    stack.pop()
stack=[]
push(stack,65)
push(stack,75)
push(stack,85)
push(stack,95)
push(stack,55)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)

