import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numArr = list(map(int, input().split()))
dp = numArr[:]

for i in range(1, n):
    dp[i] += dp[i-1]

for i in range(m):
    s, e = map(int, input().split())
    if s == e:
        print(numArr[e-1])
    elif s == 1:
        print(dp[e-1])
    else:
        print(dp[e-1] - dp[s-2])