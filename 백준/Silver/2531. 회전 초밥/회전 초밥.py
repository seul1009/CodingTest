import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
s = []
for _ in range(N):
    s.append(int(input()))

sushi = s + s
maxCount = 0

for i in range(N):
    kind = set(sushi[i:i+k])
    count = len(kind)
    if c not in kind:
        count += 1

    maxCount = max(maxCount, count)

print(maxCount)
