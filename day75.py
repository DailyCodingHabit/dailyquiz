

def createStack():
    stack = []
    return stack
def isEmpty(stack):
    return len(stack) == 0
def push(stack, item):
    stack.append(item)
def pop(stack):
    return stack.pop()

stack = createStack()
print(stack) # Output: []
push(stack, str(1))
print(stack) # Output: ['1']
push(stack, str(2))
print(stack) # Output: ['1', '2']
pop(stack) 
print(stack) # Output: ['1']