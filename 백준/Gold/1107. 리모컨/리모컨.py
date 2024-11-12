import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ans = abs(100 - n)

if m:
    btn = list(input().split())
else:
    btn = []

for num in range(1000001):
    for i in str(num):
        if i in btn:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)