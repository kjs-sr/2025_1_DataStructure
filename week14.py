import sys
n = int(input())
stack = []

for i in range(n):
  order = sys.stdin.readline().strip()
  if 'push' in order:
    number = order.split()
    stack.append(number[-1])
  elif order == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif order == 'size':
    print(len(stack))
  elif order == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif order == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])