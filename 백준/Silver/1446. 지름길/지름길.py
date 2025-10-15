import sys
input = sys.stdin.readline

n, d = map(int, input().split())
shortcuts = []

for _ in range(n):
    start, end, length = map(int, input().split())
    if end <= d and end-start > length:
        shortcuts.append((start, end, length))

shortcuts.sort()

dp = [i for i in range(d + 1)]

for i in range(d + 1):
    for s, e, l in shortcuts:
        if s == i and e <= d:
            dp[e] = min(dp[e], dp[s] + l)

    if i < d:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
print(dp[d])