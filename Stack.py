'''
The functions associated with stack are:

empty() – Returns whether the stack is empty – Time Complexity : O(1)
size() – Returns the size of the stack – Time Complexity : O(1)
top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
pop() – Deletes the top most element of the stack – Time Complexity : O(1)
'''

#Implementation using list:

stack = []

stack.append('January')
stack.append('February')
stack.append('March')
stack.append('April')

print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)

