import sys
input = sys.stdin.readline

n = int(input())
children = [int(input()) for _ in range(n)]

dp = [1] * n

for current in range(1, n):
    for previous in range(current):
        if children[previous] < children[current]:
            dp[current] = max(dp[current], dp[previous] + 1)

print(n - max(dp))

