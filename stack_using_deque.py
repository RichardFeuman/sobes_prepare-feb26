from collections import deque
stack = deque([1, 2, 3])
stack.append(4)
stack.append(5)


print(stack.pop())
print(stack.pop())
print(stack.pop())
