import sys
input = sys.stdin.readline

strings = input().rstrip()
explosion = input().rstrip()
e = len(explosion)
stack = []

for s in strings:
    stack.append(s)
    if stack[-e:] == list(explosion):
        for _ in range(e):
            stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")