'''
####  Methods Available in Queue

Python provides the following methods, which are commonly used to perform the operation in Queue.

put(item) - This function is used to insert element to the queue.
get() - This function is used to extract the element from the queue.
empty() - This function is used to check whether a queue is empty or not. It returns true if queue is empty.
qsize - This function returns the length of the queue.
full() - If the queue is full returns true; otherwise false.

'''

'''Implementation Using List'''
print('-------------Implementation Using List--------------')
que = []

que.append('CSE')
que.append('EEE')
que.append('Civil')
que.append('ECE')

print(que)

print(que.pop(0))
print(que)

print(que.pop(0))
print(que)

print(que.pop(0))
print(que)

print(que.pop(0))
print(que)


'''Implementation Using List'''
print('--------------Implementation Using List----------------')
from collections import deque

q = deque()

q.append('ML')
q.append('DS')
q.append('Soft')
q.append('Networking')

print(q)

print(q.popleft())
print(q)

print(q.popleft())
print(q)

print(q.popleft())
print(q)

print(q.popleft())
print(q)




