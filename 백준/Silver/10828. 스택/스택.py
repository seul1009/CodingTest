import sys
input = sys.stdin.readline

stack = []
n = int(input())
for _ in range(n):
    m = input().split()
    if m[0] == "push":
        stack.append(m[1])
    elif m[0] == "top":
        print(stack[-1] if len(stack) != 0 else -1)
    elif m[0] == "size":
        print(len(stack) )
    elif m[0] == "pop":
        print(stack.pop() if len(stack) != 0 else -1)
    elif m[0] == "empty":
        print(1 if len(stack) == 0 else 0)


