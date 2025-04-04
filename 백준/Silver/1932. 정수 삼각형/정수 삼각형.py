n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

DP = [[0] * (i + 1) for i in range(n)]
DP[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            DP[i][j] = DP[i-1][j] + triangle[i][j]
        elif j == i:
            DP[i][j] = DP[i-1][j-1] + triangle[i][j]
        else:
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + triangle[i][j]

print(max(DP[n-1]))
