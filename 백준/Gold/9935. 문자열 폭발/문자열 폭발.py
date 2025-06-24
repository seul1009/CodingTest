import sys
input = sys.stdin.readline

strings = input().rstrip()
explosion = input().rstrip()
e = len(explosion)
idx = 0
stack = []

while True:
    for s in strings:
        stack.append(s)
        if "".join(stack[-e:]) == explosion:
            for _ in range(e):
                stack.pop()
    break

if stack:
    print("".join(stack))
else:
    print("FRULA")